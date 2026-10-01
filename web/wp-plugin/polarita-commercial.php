<?php
/**
 * Plugin Name: Polarita Commercial Pages
 * Description: Scoped presentation and metadata for the eleven approved commercial pages.
 * Version: 1.3.7
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

require_once __DIR__ . '/holiday.php';
