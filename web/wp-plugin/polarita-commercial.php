<?php
/**
 * Plugin Name: Polarita Commercial Pages
 * Description: Scoped presentation and metadata for the eleven approved commercial pages.
 * Version: 1.4.1
 * Author: Polarita s.r.o.
 */
if (!defined('ABSPATH')) { exit; }

function polarita_commercial_pages() {
    return array(
        539 => array('Revize elektro a přezkoušení elektrikářů | Polarita', 'Revize elektro po celé ČR a školení s přezkoušením elektrikářů podle § 6 a § 7. Poučení podle § 4. Domluvte zadání s Václavem Šerclem.', 'Revize elektro a přezkoušení elektrikářů', ''),
        18 => array('Kontakt: revize a školení elektro | Polarita', 'Kontaktujte Václava Šercla: revize elektro, školení a přezkoušení elektrikářů po celé ČR. Pořadatel Polarita s.r.o. Telefon 792 779 534.', 'Kontakt', ''),
        1385 => array('Elektroinstalační práce a rozvaděče | Polarita', 'Elektroinstalační práce pro byty, domy a firmy po celé ČR. Domluvte rozvody, rozvaděče, úpravy instalace i návaznou revizi podle konkrétního zadání.', 'Elektroinstalační práce', 'Elektroinstalační práce'),
        1386 => array('Montáž wallboxů a nabíjecích stanic | Polarita', 'Výběr wallboxu, odborná montáž a revize nabíjecí stanice po celé ČR. Propojte vybavení z e-shopu Polarita.eu s instalací podle podmínek vašeho objektu.', 'Montáž wallboxů', 'Montáž wallboxů'),
        1410 => array('Revize elektroinstalací po celé ČR | Polarita', 'Revize elektroinstalací v bytech, domech a firemních objektech. Prohlídka, měření a revizní zpráva. Rozsah, cenu a termín domluvte přímo s technikem.', 'Revize elektroinstalací', 'Revize elektroinstalací'),
        1413 => array('Revize hromosvodů po celé ČR | Polarita', 'Revize hromosvodů pro rodinné a bytové domy i firmy. Kontrola ochrany před bleskem, potřebná měření a revizní zpráva podle dohodnutého rozsahu.', 'Revize hromosvodů', 'Revize hromosvodů'),
        1416 => array('Revize elektrických spotřebičů | Polarita', 'Revize elektrických spotřebičů pro kanceláře, provozovny a další pracoviště po celé ČR. Domluvte kontrolu, evidenci a termín s ohledem na váš provoz.', 'Revize elektrických spotřebičů', 'Revize elektrických spotřebičů'),
        1419 => array('Revize nabíjecích stanic a wallboxů | Polarita', 'Revize nabíjecích stanic a domácích wallboxů po celé ČR. Kontrola stanice a připojení v dohodnutém rozsahu, měření a zpracování revizní zprávy.', 'Revize nabíjecích stanic', 'Revize nabíjecích stanic'),
        1422 => array('Revize FVE a fotovoltaických elektráren | Polarita', 'Revize fotovoltaických elektráren pro domácnosti a firmy po celé ČR. Upřesníme rozsah, potřebné podklady, cenu i termín podle konkrétní FVE.', 'Revize FVE', 'Revize fotovoltaických elektráren'),
        1425 => array('Revize pro domácnosti, firmy a bytové domy | Polarita', 'Elektro revize pro domácnosti, firmy, družstva a společenství vlastníků po celé ČR. Zjistěte, jak připravit zadání podle typu objektu.', 'Pro koho', ''),
        1462 => array('Školení a zkoušky elektro § 4, 6 a 7 | Polarita', 'Poučení podle § 4 a školení s přezkoušením podle § 6 a § 7 pro firmy a živnostníky. Zaměření E2A, celé Česko. Domluvte rozsah a termín.', 'Školení a zkoušky elektro', ''),
    );
}

function polarita_commercial_current() {
    if (is_admin() || is_feed() || is_preview() || !is_page()) { return false; }
    $pages = polarita_commercial_pages();
    $id = get_queried_object_id();
    return isset($pages[$id]) ? $pages[$id] : false;
}

function polarita_commercial_title($title) {
    $page = polarita_commercial_current();
    return $page ? $page[0] : $title;
}
add_filter('pre_get_document_title', 'polarita_commercial_title', 99);

function polarita_commercial_template($template) {
    return polarita_commercial_current() ? __DIR__ . '/template.php' : $template;
}
add_filter('template_include', 'polarita_commercial_template', 99);

function polarita_commercial_prepare() {
    if (!polarita_commercial_current()) { return; }
    remove_action('wp_head', 'rel_canonical');
    remove_filter('the_content', 'sharing_display', 19);
    remove_filter('the_excerpt', 'sharing_display', 19);
    add_filter('jetpack_enable_open_graph', '__return_false');
    add_filter('wpl_is_enabled_sitewide', '__return_false');
}
add_action('wp', 'polarita_commercial_prepare');

function polarita_commercial_assets() {
    if (!polarita_commercial_current()) { return; }
    foreach (array('twentyfifteen-script', 'jetpack-likes', 'sharing-js', 'stats', 'jetpack-stats') as $handle) {
        wp_dequeue_script($handle);
    }
    foreach (array('twentyfifteen-style', 'twentyfifteen-block-style', 'twentyfifteen-jetpack', 'twentyfifteen-fonts', 'genericons', 'sharedaddy', 'social-logos', 'jetpack_likes') as $handle) {
        wp_dequeue_style($handle);
    }
}
add_action('wp_enqueue_scripts', 'polarita_commercial_assets', 999);
add_action('wp_print_footer_scripts', 'polarita_commercial_assets', 1);
// Recheck after all enqueue callbacks, before WordPress prints styles.
add_action('wp_print_styles', 'polarita_commercial_assets', 0);

function polarita_commercial_metadata() {
    $page = polarita_commercial_current();
    if (!$page) { return; }
    $id = get_queried_object_id();
    // Public site ownership token supplied by Bing Webmaster Tools.
    if ($id === 539) { echo '<meta name="msvalidate.01" content="57D718E34DBE413FA70D99F3B965A9A8">' . "\n"; }
    $url = get_permalink($id);
    $home = home_url('/');
    $logo = plugins_url('assets/polarita-logo.jpg', __FILE__);
    echo '<meta name="description" content="' . esc_attr($page[1]) . '">' . "\n";
    echo '<link rel="canonical" href="' . esc_url($url) . '">' . "\n";
    foreach (array('og:type'=>'website','og:locale'=>'cs_CZ','og:site_name'=>'Polarita','og:title'=>$page[0],'og:description'=>$page[1],'og:url'=>$url,'og:image'=>$logo,'og:image:alt'=>'Logo Polarita') as $key=>$value) {
        echo '<meta property="' . esc_attr($key) . '" content="' . esc_attr($value) . '">' . "\n";
    }
    echo '<meta name="twitter:card" content="summary">' . "\n";
    $organization = array('@type'=>'Organization','@id'=>$home.'#organization','name'=>'Polarita s.r.o.','url'=>$home,'logo'=>$logo,'telephone'=>'+420792779534','email'=>'vaclav.sercl@polarita.cz','taxID'=>'CZ14180324','identifier'=>'14180324','address'=>array('@type'=>'PostalAddress','streetAddress'=>'Na Folimance 2155/15','addressLocality'=>'Praha 2','postalCode'=>'120 00','addressCountry'=>'CZ'),'contactPoint'=>array('@type'=>'ContactPoint','telephone'=>'+420792779534','email'=>'vaclav.sercl@polarita.cz','contactType'=>'customer service','availableLanguage'=>'cs','areaServed'=>'CZ'));
    $organization['sameAs'] = array('https://www.facebook.com/polarita.cz/', 'https://www.youtube.com/@polarita2983');
    $person = array('@type'=>'Person','@id'=>$home.'#vaclav-sercl','name'=>'Václav Šercl','jobTitle'=>'Revizní technik elektro','url'=>home_url('/kontakt/').'#vaclav-sercl','worksFor'=>array('@id'=>$home.'#organization'),'sameAs'=>array('https://x.com/VaclavSercl','https://www.linkedin.com/in/vaclav-sercl/'));
    $graph = array($organization, $person, array('@type'=>'WebSite','@id'=>$home.'#website','url'=>$home,'name'=>'Polarita','inLanguage'=>'cs','publisher'=>array('@id'=>$home.'#organization')));
    $crumbs = array(array('@type'=>'ListItem','position'=>1,'name'=>'Polarita','item'=>$home));
    if ($id !== 539) { $crumbs[] = array('@type'=>'ListItem','position'=>2,'name'=>$page[2],'item'=>$url); }
    $graph[] = array('@type'=>'BreadcrumbList','@id'=>$url.'#breadcrumb','itemListElement'=>$crumbs);
    $graph[] = array('@type'=>'WebPage','@id'=>$url.'#webpage','url'=>$url,'name'=>$page[0],'description'=>$page[1],'inLanguage'=>'cs','isPartOf'=>array('@id'=>$home.'#website'),'breadcrumb'=>array('@id'=>$url.'#breadcrumb'),'about'=>array('@id'=>$home.'#organization'),'dateModified'=>get_post_modified_time('c', true, $id));
    if ($page[3] !== '') { $graph[] = array('@type'=>'Service','@id'=>$url.'#service','name'=>$page[3],'serviceType'=>$page[3],'url'=>$url,'provider'=>array('@id'=>$home.'#organization'),'areaServed'=>array('@type'=>'Country','name'=>'Česká republika')); }
    echo '<script type="application/ld+json">' . wp_json_encode(array('@context'=>'https://schema.org','@graph'=>$graph), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP) . '</script>' . "\n";
}
add_action('wp_head', 'polarita_commercial_metadata', 5);

function polarita_commercial_cookie_strings($strings) {
    if (!polarita_commercial_current()) { return $strings; }
    return array_merge($strings, array(
        'powered_by'=>'Technologie', 'reconsent'=>'Změnit nastavení cookies',
        'cookie_preferences'=>'Nastavení cookies', 'remark_standard'=>'Vždy aktivní',
        'remark'=>'', 'none'=>'Žádné položky v evidenci',
        'necessary_cookies'=>'Nezbytné cookies',
        'necessary_cookies_desc'=>'Zajišťují základní funkce webu, například zabezpečení přihlášení a zapamatování nastavení soukromí.',
        'functional_cookies'=>'Funkční cookies',
        'functional_cookies_desc'=>'Slouží k volitelným funkcím, například sdílení obsahu a nástrojům třetích stran.',
        'analytical_cookies'=>'Analytické cookies',
        'analytical_cookies_desc'=>'Slouží k měření návštěvnosti a způsobu používání webu.',
        'advertisement_cookies'=>'Reklamní cookies',
        'advertisement_cookies_desc'=>'Slouží k personalizaci reklamy a měření reklamních kampaní.',
        'unclassified_cookies'=>'Nezařazené cookies',
        'unclassified_cookies_desc'=>'Položky, u kterých dosud není dokončeno zařazení podle účelu.'
    ));
}
add_filter('cookieadmin_default_strings', 'polarita_commercial_cookie_strings');

function polarita_commercial_logo($content) {
    if (!polarita_commercial_current()) { return $content; }
    $logo = '<a class="pk-logo" href="' . esc_url(home_url('/')) . '" aria-label="Polarita – úvod"><img src="' . esc_url(plugins_url('assets/polarita-logo.jpg', __FILE__)) . '" width="128" height="128" alt="Polarita" decoding="async"></a>';
    return preg_replace('/<a\b[^>]*class="pk-logo"[^>]*>.*?<\/a>/s', $logo, $content);
}
add_filter('the_content', 'polarita_commercial_logo', 30);

// Exclude only the commercial training landing page from Google News.
// Leave the normal sitemap and every other page unchanged.
function polarita_commercial_news_skip($skip, $post) {
    return $skip || (isset($post->ID) && (int) $post->ID === 1462);
}
add_filter('jetpack_sitemap_news_skip_post', 'polarita_commercial_news_skip', 10, 2);

// Jetpack otherwise flushes this cache only for posts, not updated pages.
function polarita_commercial_news_refresh($post_id) {
    if ((int) $post_id === 1462) {
        delete_transient('jetpack_news_sitemap_xml');
    }
}
add_action('save_post_page', 'polarita_commercial_news_refresh');

// Existing CMP extension point. Only commercial pages receive these two entries.
function polarita_commercial_cookie_policy($policy) {
    if (!polarita_commercial_current()) { return $policy; }
    if (!is_array($policy) || !isset($policy['categorized_cookies']) || !is_array($policy['categorized_cookies'])) { return $policy; }
    foreach (array('_ga', '_ga_XSS8H12Z36') as $name) {
        $policy['categorized_cookies'][$name] = array('cookie_name'=>$name, 'category'=>'analytics', 'description'=>'Google Analytics: měření návštěvnosti a používání komerčních stránek pouze po souhlasu. Platnost nejvýše 180 dnů.', 'platform'=>'Google Analytics', 'expires'=>gmdate('Y-m-d\TH:i:s\Z', time() + 15552000), 'patterns'=>'');
    }
    return $policy;
}
add_filter('cookieadmin_before_localize', 'polarita_commercial_cookie_policy');

function polarita_commercial_indexnow_key() {
    $key = get_option('polarita_indexnow_key', '');
    return is_string($key) && preg_match('/^[a-f0-9]{32}$/D', $key) ? $key : '';
}
function polarita_commercial_indexnow_init() {
    if (current_user_can('manage_options') && home_url('/') === 'https://www.polarita.cz/' && !polarita_commercial_indexnow_key()) {
        add_option('polarita_indexnow_key', str_replace('-', '', wp_generate_uuid4()), '', false);
    }
}
add_action('admin_init', 'polarita_commercial_indexnow_init');

function polarita_commercial_indexnow_proof() {
    $key = polarita_commercial_indexnow_key();
    $path = isset($_SERVER['REQUEST_URI']) ? wp_parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH) : '';
    if (!$key || home_url('/') !== 'https://www.polarita.cz/' || $path !== '/'.$key.'.txt') { return; }
    status_header(200);
    header('Content-Type: text/plain; charset=utf-8');
    header('X-Robots-Tag: noindex');
    echo $key;
    exit;
}
add_action('template_redirect', 'polarita_commercial_indexnow_proof', 0);

function polarita_commercial_indexnow_send($ids, $attempt = 0) {
    $key = polarita_commercial_indexnow_key();
    if (!$key || home_url('/') !== 'https://www.polarita.cz/' || $attempt > 2) { return; }
    $pages = polarita_commercial_pages();
    $urls = array();
    $valid_ids = array();
    foreach (array_unique(array_map('intval', (array) $ids)) as $id) {
        if (!isset($pages[$id]) || get_post_status($id) !== 'publish') { continue; }
        $url = get_permalink($id);
        if (wp_parse_url($url, PHP_URL_HOST) !== 'www.polarita.cz' || wp_parse_url($url, PHP_URL_SCHEME) !== 'https') { continue; }
        $urls[] = $url;
        $valid_ids[] = $id;
    }
    if (!$urls) { return; }
    $response = wp_remote_post('https://api.indexnow.org/indexnow', array('timeout'=>12, 'redirection'=>0, 'headers'=>array('Content-Type'=>'application/json; charset=utf-8'), 'body'=>wp_json_encode(array('host'=>'www.polarita.cz', 'key'=>$key, 'keyLocation'=>home_url('/'.$key.'.txt'), 'urlList'=>$urls))));
    $code = is_wp_error($response) ? 0 : (int) wp_remote_retrieve_response_code($response);
    update_option('polarita_indexnow_status', array('time'=>gmdate('c'), 'code'=>$code, 'count'=>count($urls), 'attempt'=>$attempt + 1), false);
    if (($code === 0 || $code === 429 || $code >= 500) && $attempt < 2) {
        wp_schedule_single_event(time() + (300 * ($attempt + 1)), 'polarita_commercial_indexnow_retry', array($valid_ids, $attempt + 1));
    }
}
add_action('polarita_commercial_indexnow_retry', 'polarita_commercial_indexnow_send', 10, 2);

function polarita_commercial_indexnow_saved($id, $post, $update) {
    if (wp_is_post_revision($id) || wp_is_post_autosave($id) || $post->post_status !== 'publish') { return; }
    $pages = polarita_commercial_pages();
    if (!isset($pages[$id]) || !polarita_commercial_indexnow_key()) { return; }
    $fingerprint = hash('sha256', $post->post_title."\n".$post->post_content."\n".get_permalink($id));
    if (get_post_meta($id, '_polarita_indexnow_content', true) === $fingerprint) { return; }
    update_post_meta($id, '_polarita_indexnow_content', $fingerprint);
    $args = array(array((int)$id), 0);
    if (!wp_next_scheduled('polarita_commercial_indexnow_retry', $args)) {
        wp_schedule_single_event(time() + 60, 'polarita_commercial_indexnow_retry', $args);
    }
}
add_action('save_post_page', 'polarita_commercial_indexnow_saved', 20, 3);

function polarita_commercial_seo_menu() {
    add_management_page('Polarita SEO', 'Polarita SEO', 'manage_options', 'polarita-seo', 'polarita_commercial_seo_screen');
}
add_action('admin_menu', 'polarita_commercial_seo_menu');
function polarita_commercial_seo_screen() {
    if (!current_user_can('manage_options')) { return; }
    if (isset($_POST['polarita_indexnow_submit'])) {
        check_admin_referer('polarita_indexnow_submit');
        if (!get_transient('polarita_indexnow_manual')) {
            set_transient('polarita_indexnow_manual', 1, 300);
            polarita_commercial_indexnow_send(array_keys(polarita_commercial_pages()));
        }
    }
    $status = get_option('polarita_indexnow_status', array());
    echo '<div class="wrap"><h1>Polarita SEO</h1><p>IndexNow: pouze publikované komerční stránky. 200 = přijato, 202 = čeká ověření klíče. Přijetí není potvrzení indexace.</p>';
    if ($status) { echo '<p>Poslední odpověď HTTP: '.esc_html($status['code']).'; počet URL: '.esc_html($status['count']).'; pokus: '.esc_html($status['attempt']).'; UTC: '.esc_html($status['time']).'</p>'; }
    $key = polarita_commercial_indexnow_key();
    if ($key) { echo '<p><a href="'.esc_url(home_url('/'.$key.'.txt')).'">Ověřit textový soubor vlastnictví</a></p>'; }
    echo '<form method="post">';
    wp_nonce_field('polarita_indexnow_submit');
    echo '<button class="button button-primary" name="polarita_indexnow_submit" value="1">Odeslat komerční URL do IndexNow</button></form></div>';
}

function polarita_commercial_conversions() {
    if (!polarita_commercial_current()) { return; }
    echo '<script id="polarita-conversions">';
    echo <<<'POLARITA_CONVERSIONS'
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

POLARITA_CONVERSIONS;
    echo '</script>';
}
add_action('wp_footer', 'polarita_commercial_conversions', 90);

require_once __DIR__ . '/holiday.php';
