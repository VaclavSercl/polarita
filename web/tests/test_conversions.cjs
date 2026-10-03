'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync('web/wp-plugin/conversions.js', 'utf8');
function setup(consent) {
  const listeners = {}, scripts = [], timers = [];
  let mutation, reloads = 0, succeeded = false;
  const result = {getAttribute:()=>succeeded?null:'true'};
  const wrapper = {querySelector:()=>succeeded?result:null};
  const doc = {
    cookie:consent === undefined?'':`cookieadmin_consent=${encodeURIComponent(JSON.stringify(consent))}`,
    head:{appendChild:s=>scripts.push(s)}, body:{},
    querySelector:()=>({href:'https://www.polarita.cz/'}),
    querySelectorAll:()=>[wrapper],createElement:()=>({}),
    addEventListener:(name,fn)=>listeners[name]=fn
  };
  const win = {location:{href:'https://www.polarita.cz/?email=private@example.com#private',reload:()=>reloads++},addEventListener:()=>{}};
  vm.runInNewContext(source,{document:doc,window:win,URL,Date,WeakSet,setTimeout:fn=>fn(),setInterval:fn=>timers.push(fn),MutationObserver:class {constructor(fn){mutation=fn;} observe(){}}});
  return {doc,win,scripts,change:c=>{doc.cookie='cookieadmin_consent='+encodeURIComponent(JSON.stringify(c));timers[0]();},events:()=>Array.from(win.dataLayer||[],x=>Array.from(x)).filter(x=>x[0]==='event'),
    click:href=>listeners.click({target:{closest:s=>s==='a'?{getAttribute:()=>href,classList:{contains:()=>true}}:null}}),
    submit:()=>listeners.submit({target:{matches:()=>true,closest:()=>wrapper}}),
    success:()=>{succeeded=true;mutation();},mutate:()=>mutation(),reloads:()=>reloads};
}
for(const consent of [undefined,{reject:'true'},{analytics:'false'},{functional:true},{marketing:true},{accept:true,reject:true}]){
  const t=setup(consent); t.click('tel:+420792779534'); t.submit(); t.success();
  assert.equal(t.scripts.length,0); assert.equal(t.events().length,0);
}
let t=setup({analytics:'true'});
assert.equal(t.scripts.length,1); assert.equal(t.events().length,1);
t.success(); assert.equal(t.events().filter(e=>e[1]==='generate_lead').length,0,'pre-existing success is not a lead');
t.submit();t.mutate();assert.equal(t.events().filter(e=>e[1]==='generate_lead').length,0,'old success cannot become a new lead after submit');
t=setup({accept:true}); t.submit(); t.success(); t.mutate();
assert.equal(t.events().filter(e=>e[1]==='generate_lead').length,1);
t.click('tel:+420792779534');t.click('mailto:private@example.com');t.click('https://www.polarita.eu/product/?private=value');
assert.deepEqual(t.events().slice(-3).map(e=>e[1]),['click_phone','click_email','click_shop']);
assert(!JSON.stringify(t.win.dataLayer).includes('private'),'PII in URL/link must never enter telemetry');
t.change({reject:true});t.click('tel:+420792779534');
assert.equal(t.reloads(),1);assert.equal(t.win['ga-disable-G-XSS8H12Z36'],true);
assert.equal(t.events().filter(e=>e[1]==='click_phone').length,1);
t=setup();t.click('tel:+420792779534');t.change({analytics:true});
assert.equal(t.scripts.length,1);assert.equal(t.events().filter(e=>e[1]==='click_phone').length,0,'no replay');
t.doc.cookie='cookieadmin_consent=%broken';t.click('tel:+420792779534');
assert.equal(t.win['ga-disable-G-XSS8H12Z36'],true);
const plugin=fs.readFileSync('web/wp-plugin/polarita-commercial.php','utf8');
assert(plugin.includes(source),'deployed inline source must equal tested source');
console.log('PASS: consent, restored opt-in, reject, revocation, no replay/PII, success-only lead, dedupe, embedded source');
