/* Tested source embedded in polarita-commercial.php; no separate server file required. */
(function () {
  'use strict';
  const id = 'G-XSS8H12Z36';
  const disabled = 'ga-disable-' + id;
  let loaded = false, active = false;
  const attempts = new WeakSet(), completed = new WeakSet();
  function allowed() {
    try {
      const raw = document.cookie.split(';').map(x => x.trim()).find(x => x.startsWith('cookieadmin_consent='));
      if (!raw) return false;
      const consent = JSON.parse(decodeURIComponent(raw.slice('cookieadmin_consent='.length)));
      const yes = value => value === true || value === 'true';
      return !yes(consent.reject) && (yes(consent.accept) || yes(consent.analytics));
    } catch (_) { return false; }
  }
  function eraseCookies() {
    for (const name of ['_ga', '_ga_XSS8H12Z36']) {
      for (const domain of ['', '; domain=www.polarita.cz', '; domain=.polarita.cz']) {
        document.cookie = name + '=; Max-Age=0; path=/; SameSite=Lax; Secure' + domain;
      }
    }
  }
  function reconcile() {
    const consent = allowed();
    window[disabled] = !consent;
    if (!consent) {
      if (active) {
        active = false;
        eraseCookies();
        // Remove the already-loaded library on revocation, with no denied-state pings.
        window.location.reload();
      }
      return false;
    }
    active = true;
    if (!loaded) {
      loaded = true;
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag('consent', 'default', {analytics_storage:'denied',ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied'});
      window.gtag('consent', 'update', {analytics_storage:'granted',ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied'});
      window.gtag('js', new Date());
      // Canonical path only: never send search/hash, referrer or a form-derived title.
      const canonical = document.querySelector('link[rel="canonical"]');
      const url = new URL(canonical ? canonical.href : window.location.href);
      window.gtag('config', id, {send_page_view:false,allow_google_signals:false,allow_ad_personalization_signals:false,cookie_domain:'www.polarita.cz',cookie_expires:15552000,page_location:url.origin+url.pathname,page_referrer:'',page_title:'Polarita'});
      window.gtag('event', 'page_view', {page_location:url.origin+url.pathname,page_referrer:'',page_title:'Polarita'});
      const script = document.createElement('script');
      script.async = true;
      script.src = 'https://www.googletagmanager.com/gtag/js?id=' + id;
      document.head.appendChild(script);
    }
    return true;
  }
  function event(name, params) {
    if (reconcile() && active) window.gtag('event', name, params || {});
  }
  document.addEventListener('click', function (e) {
    const anchor = e.target.closest('a');
    if (anchor && reconcile()) {
      const href = anchor.getAttribute('href') || '';
      if (href.startsWith('tel:')) event('click_phone');
      else if (href.startsWith('mailto:')) event('click_email');
      else if (/^https:\/\/www\.polarita\.eu(?:\/|$)/.test(href)) event('click_shop');
      else if (anchor.classList.contains('pk-btn')) event('click_cta', {cta_group:href.includes('skoleni')?'training':href.includes('wallbox')||href.includes('elektroinstalace')?'installation':'service'});
    }
    if (e.target.closest('.cookieadmin_save_btn,.cookieadmin_accept_btn,.cookieadmin_reject_btn')) setTimeout(reconcile, 0);
  }, true);
  document.addEventListener('submit', function (e) {
    if (!e.target.matches('form.jetpack-contact-form__form')) return;
    const wrapper = e.target.closest('[data-wp-interactive="jetpack/form"]');
    if (wrapper && allowed() && !wrapper.querySelector('.contact-form-ajax-submission.submission-success')) attempts.add(wrapper);
  }, true);
  function success() {
    for (const wrapper of document.querySelectorAll('[data-wp-interactive="jetpack/form"]')) {
      const result = wrapper.querySelector('.contact-form-ajax-submission.submission-success');
      if (!attempts.has(wrapper) || completed.has(wrapper) || !result || result.getAttribute('aria-hidden') === 'true') continue;
      completed.add(wrapper);
      event('generate_lead', {form_type:'commercial_enquiry'});
    }
  }
  new MutationObserver(success).observe(document.body, {subtree:true,attributes:true,attributeFilter:['class','aria-hidden']});
  document.addEventListener('visibilitychange', reconcile);
  window.addEventListener('pageshow', reconcile);
  setInterval(reconcile, 1000);
  reconcile();
})();
