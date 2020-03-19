<!DOCTYPE html>
<html class="" lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="Web Scraping with Python and BeautifulSoup/Web Scraping with Python and Beautiful Soup.py · master · Data Science Dojo / tutorials" property="og:title">
<meta content="Data science code, datasets and more" property="og:description">
<meta content="/uploads/-/system/project/avatar/80/man-reading.png" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://code.datasciencedojo.com/datasciencedojo/tutorials/blob/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="Web Scraping with Python and BeautifulSoup/Web Scraping with Python and Beautiful Soup.py · master · Data Science Dojo / tutorials" property="twitter:title">
<meta content="Data science code, datasets and more" property="twitter:description">
<meta content="/uploads/-/system/project/avatar/80/man-reading.png" property="twitter:image">

<title>Web Scraping with Python and BeautifulSoup/Web Scraping with Python and Beautiful Soup.py · master · Data Science Dojo / tutorials · GitLab</title>
<meta content="Data science code, datasets and more" name="description">
<link rel="shortcut icon" type="image/x-icon" href="/assets/favicon-3b9d47a9a355ceea06a542b78dc1f3ac8f1756f624768accaf05fe105713f542.ico" id="favicon" />
<link rel="stylesheet" media="all" href="/assets/application-38faeff5f0e763c1b0725454bae36fc32a1106938d1ff9511c26b11bfad4c3f1.css" />
<link rel="stylesheet" media="print" href="/assets/print-74b3d49adeaada27337e759b75a34af7cf3d80051de91d60d40570f5a382e132.css" />


<script>
//<![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https:\/\/code.datasciencedojo.com\/assets\/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=1000;gon.asset_host=null;gon.webpack_public_path="\/assets\/webpack\/";gon.relative_url_root="";gon.shortcuts_path="\/help\/shortcuts";gon.user_color_scheme="white";gon.gitlab_url="https:\/\/code.datasciencedojo.com";gon.revision="dee2c87";gon.gitlab_logo="\/assets\/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png";gon.sprite_icons="\/assets\/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg";gon.sprite_file_icons="\/assets\/file_icons-7262fc6897e02f1ceaf8de43dc33afa5e4f9a2067f4f68ef77dcc87946575e9e.svg";gon.test_env=false;gon.suggested_label_colors=["#0033CC","#428BCA","#44AD8E","#A8D695","#5CB85C","#69D100","#004E00","#34495E","#7F8C8D","#A295D6","#5843AD","#8E44AD","#FFECDB","#AD4363","#D10069","#CC0033","#FF0000","#D9534F","#D1D100","#F0AD4E","#AD8D43"];
//]]>
</script>

<script src="/assets/webpack/webpack_runtime.bf993a5b9d06faed3c70.bundle.js" defer="defer"></script>
<script src="/assets/webpack/common.db159cd75479db13c6a5.bundle.js" defer="defer"></script>
<script src="/assets/webpack/main.b9fa1bb4b84fda196c23.bundle.js" defer="defer"></script>

<script src="/assets/webpack/pages.projects.01592773ca8dd5701db7.bundle.js" defer="defer"></script>
<script src="/assets/webpack/pages.projects.blob.show.c156a41fbff24f4bce1a.bundle.js" defer="defer"></script>

<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="qXVA/frInLnN4SPIJypwP1+jgxJ9NfcAi0lkWsIQbWj9p0LQNxmBvUXjGBBoWWdNy0hah1CBk1Dpg+1qu6F0xQ==" />
<meta content="origin-when-cross-origin" name="referrer">
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#474D57" name="theme-color">
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-5a9cee0e8a51212e70b90c87c12f382c428870c0ff67d1eb034d884b78d2dae7.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-a6eec6aeb9da138e507593b464fdac213047e49d3093fc30e90d9a995df83ba3.png" sizes="76x76" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-retina-72e2aadf86513a56e050e7f0f2355deaa19cc17ed97bbe5147847f2748e5a3e3.png" sizes="120x120" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-retina-8ebe416f5313483d9c1bc772b5bbe03ecad52a54eba443e5215a22caed2a16a2.png" sizes="152x152" />
<link color="rgb(226, 67, 41)" href="/assets/logo-d36b5212042cebc89b96df4bf6ac24e43db316143e89926c0db839ff694d2de4.svg" rel="mask-icon">
<meta content="/assets/msapplication-tile-1196ec67452f618d39cdd85e2e3a542f76574c071051ae7effbfde01710eb17d.png" name="msapplication-TileImage">
<meta content="#30353E" name="msapplication-TileColor">



<script nonce="true">
//<![CDATA[
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});
var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';
j.async=true;
j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-597X89S');

//]]>
</script></head>

<body class="ui_indigo " data-find-file="/datasciencedojo/tutorials/find_file/master" data-group="" data-page="projects:blob:show" data-project="tutorials">
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-597X89S" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>


<header class="navbar navbar-gitlab qa-navbar">
<a class="sr-only gl-accessibility" href="#content-body" tabindex="1">Skip to content</a>
<div class="container-fluid">
<div class="header-content">
<div class="title-container">
<h1 class="title">
<a title="Dashboard" id="logo" href="/"><img data-src="/uploads/-/system/appearance/header_logo/1/cropped-Logo_Tori.png" class=" lazy" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />
</a></h1>
<ul class="list-unstyled navbar-sub-nav">
<li class="home"><a title="Projects" class="dashboard-shortcuts-projects" href="/explore">Projects
</a></li><li class=""><a title="Groups" class="dashboard-shortcuts-groups" href="/explore/groups">Groups
</a></li><li class=""><a title="Snippets" class="dashboard-shortcuts-snippets" href="/explore/snippets">Snippets
</a></li><li>
<a title="About GitLab CE" href="/help">Help</a>
</li>
</ul>

</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li class="hidden-sm hidden-xs">
<div class="has-location-badge search search-form">
<form class="navbar-form" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><div class="search-input-container">
<div class="location-badge">This project</div>
<div class="search-input-wrap">
<div class="dropdown" data-url="/search/autocomplete">
<input type="search" name="search" id="search" placeholder="Search" class="search-input dropdown-menu-toggle no-outline js-search-dashboard-options" spellcheck="false" tabindex="1" autocomplete="off" data-issues-path="/dashboard/issues" data-mr-path="/dashboard/merge_requests" aria-label="Search" />
<button class="hidden js-dropdown-search-toggle" data-toggle="dropdown" type="button"></button>
<div class="dropdown-menu dropdown-select">
<div class="dropdown-content"><ul>
<li class="dropdown-menu-empty-item">
<a>
Loading...
</a>
</li>
</ul>
</div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
<svg class="s16 search-icon"><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#search"></use></svg>
<svg class="s16 clear-icon js-clear-input"><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#close"></use></svg>
</div>
</div>
</div>
<input type="hidden" name="group_id" id="group_id" class="js-search-group-options" />
<input type="hidden" name="project_id" id="search_project_id" value="80" class="js-search-project-options" data-project-path="tutorials" data-name="tutorials" data-issues-path="/datasciencedojo/tutorials/issues" data-mr-path="/datasciencedojo/tutorials/merge_requests" data-issues-disabled="false" />
<input type="hidden" name="search_code" id="search_code" value="true" />
<input type="hidden" name="repository_ref" id="repository_ref" value="master" />

<div class="search-autocomplete-opts hide" data-autocomplete-path="/search/autocomplete" data-autocomplete-project-id="80" data-autocomplete-project-ref="master"></div>
</form></div>

</li>
<li class="visible-sm-inline-block visible-xs-inline-block">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/search"><svg class="s16"><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#search"></use></svg>
</a></li>
<li>
<div>
<a class="btn btn-sign-in" href="/users/sign_in?redirect_to_referer=yes">Sign in / Register</a>
<!-- %a.btn.btn-sign-in{ href: "/users/auth/dojo_login?redirect_to_referer=yes", tabindex: "1" } Skip to content -->
</div>
</li>
</ul>
</div>
<button class="navbar-toggle hidden-sm hidden-md hidden-lg" type="button">
<span class="sr-only">Toggle navigation</span>
<svg class="s12 more-icon js-navbar-toggle-right"><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#more"></use></svg>
<svg class="s12 close-icon js-navbar-toggle-left"><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#close"></use></svg>
</button>
</div>
</div>
</header>

<div class="layout-page page-with-contextual-sidebar">
<div class="nav-sidebar">
<div class="nav-sidebar-inner-scroll">
<div class="context-header">
<a title="tutorials" href="/datasciencedojo/tutorials"><div class="avatar-container s40 project-avatar">
<img alt="tutorials" class="avatar s40 avatar-tile lazy" data-src="/uploads/-/system/project/avatar/80/man-reading.png" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />
</div>
<div class="sidebar-context-title">
tutorials
</div>
</a></div>
<ul class="sidebar-top-level-items">
<li class="home"><a class="shortcuts-project" href="/datasciencedojo/tutorials"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#project"></use></svg>
</div>
<span class="nav-item-name">
Overview
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/datasciencedojo/tutorials"><strong class="fly-out-top-item-name">
Overview
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Project details" class="shortcuts-project" href="/datasciencedojo/tutorials"><span>Details</span>
</a></li><li class=""><a title="Activity" class="shortcuts-project-activity" href="/datasciencedojo/tutorials/activity"><span>Activity</span>
</a></li><li class=""><a title="Cycle Analytics" class="shortcuts-project-cycle-analytics" href="/datasciencedojo/tutorials/cycle_analytics"><span>Cycle Analytics</span>
</a></li></ul>
</li><li class="active"><a class="shortcuts-tree" href="/datasciencedojo/tutorials/tree/master"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#doc_text"></use></svg>
</div>
<span class="nav-item-name">
Repository
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item active"><a href="/datasciencedojo/tutorials/tree/master"><strong class="fly-out-top-item-name">
Repository
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class="active"><a href="/datasciencedojo/tutorials/tree/master">Files
</a></li><li class=""><a href="/datasciencedojo/tutorials/commits/master">Commits
</a></li><li class=""><a href="/datasciencedojo/tutorials/branches">Branches
</a></li><li class=""><a href="/datasciencedojo/tutorials/tags">Tags
</a></li><li class=""><a href="/datasciencedojo/tutorials/graphs/master">Contributors
</a></li><li class=""><a href="/datasciencedojo/tutorials/network/master">Graph
</a></li><li class=""><a href="/datasciencedojo/tutorials/compare?from=master&amp;to=master">Compare
</a></li><li class=""><a href="/datasciencedojo/tutorials/graphs/master/charts">Charts
</a></li></ul>
</li><li class=""><a class="shortcuts-issues" href="/datasciencedojo/tutorials/issues"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#issues"></use></svg>
</div>
<span class="nav-item-name">
Issues
</span>
<span class="badge count issue_counter">
0
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/datasciencedojo/tutorials/issues"><strong class="fly-out-top-item-name">
Issues
</strong>
<span class="badge count issue_counter fly-out-badge">
0
</span>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Issues" href="/datasciencedojo/tutorials/issues"><span>
List
</span>
</a></li><li class=""><a title="Board" href="/datasciencedojo/tutorials/boards"><span>
Board
</span>
</a></li><li class=""><a title="Labels" href="/datasciencedojo/tutorials/labels"><span>
Labels
</span>
</a></li><li class=""><a title="Milestones" href="/datasciencedojo/tutorials/milestones"><span>
Milestones
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-merge_requests" href="/datasciencedojo/tutorials/merge_requests"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#git-merge"></use></svg>
</div>
<span class="nav-item-name">
Merge Requests
</span>
<span class="badge count merge_counter js-merge-counter">
0
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/datasciencedojo/tutorials/merge_requests"><strong class="fly-out-top-item-name">
Merge Requests
</strong>
<span class="badge count merge_counter js-merge-counter fly-out-badge">
0
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-pipelines" href="/datasciencedojo/tutorials/pipelines"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#pipeline"></use></svg>
</div>
<span class="nav-item-name">
CI / CD
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/datasciencedojo/tutorials/pipelines"><strong class="fly-out-top-item-name">
CI / CD
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Pipelines" class="shortcuts-pipelines" href="/datasciencedojo/tutorials/pipelines"><span>
Pipelines
</span>
</a></li><li class=""><a title="Jobs" class="shortcuts-builds" href="/datasciencedojo/tutorials/-/jobs"><span>
Jobs
</span>
</a></li><li class=""><a title="Schedules" class="shortcuts-builds" href="/datasciencedojo/tutorials/pipeline_schedules"><span>
Schedules
</span>
</a></li><li class=""><a title="Charts" class="shortcuts-pipelines-charts" href="/datasciencedojo/tutorials/pipelines/charts"><span>
Charts
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-wiki" href="/datasciencedojo/tutorials/wikis/home"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#book"></use></svg>
</div>
<span class="nav-item-name">
Wiki
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/datasciencedojo/tutorials/wikis/home"><strong class="fly-out-top-item-name">
Wiki
</strong>
</a></li></ul>
</li><li class=""><a class="shortcuts-snippets" href="/datasciencedojo/tutorials/snippets"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#snippet"></use></svg>
</div>
<span class="nav-item-name">
Snippets
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/datasciencedojo/tutorials/snippets"><strong class="fly-out-top-item-name">
Snippets
</strong>
</a></li></ul>
</li><li class=""><a title="Members" class="shortcuts-tree" href="/datasciencedojo/tutorials/settings/members"><div class="nav-icon-container">
<svg><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#users"></use></svg>
</div>
<span class="nav-item-name">
Members
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/datasciencedojo/tutorials/project_members"><strong class="fly-out-top-item-name">
Members
</strong>
</a></li></ul>
</li><a class="toggle-sidebar-button js-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<svg class=" icon-angle-double-left"><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#angle-double-left"></use></svg>
<svg class=" icon-angle-double-right"><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#angle-double-right"></use></svg>
<span class="collapse-text">Collapse sidebar</span>
</a>
<button name="button" type="button" class="close-nav-button"><svg class="s16"><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#close"></use></svg>
<span class="collapse-text">Close sidebar</span>
</button>
<li class="hidden">
<a title="Activity" class="shortcuts-project-activity" href="/datasciencedojo/tutorials/activity"><span>
Activity
</span>
</a></li>
<li class="hidden">
<a title="Network" class="shortcuts-network" href="/datasciencedojo/tutorials/network/master">Graph
</a></li>
<li class="hidden">
<a title="Charts" class="shortcuts-repository-charts" href="/datasciencedojo/tutorials/graphs/master/charts">Charts
</a></li>
<li class="hidden">
<a class="shortcuts-new-issue" href="/datasciencedojo/tutorials/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a title="Jobs" class="shortcuts-builds" href="/datasciencedojo/tutorials/-/jobs">Jobs
</a></li>
<li class="hidden">
<a title="Commits" class="shortcuts-commits" href="/datasciencedojo/tutorials/commits/master">Commits
</a></li>
<li class="hidden">
<a title="Issue Boards" class="shortcuts-issue-boards" href="/datasciencedojo/tutorials/boards">Issue Boards</a>
</li>
</ul>
</div>
</div>

<div class="content-wrapper">

<div class="mobile-overlay"></div>
<div class="alert-wrapper">


<nav class="breadcrumbs container-fluid container-limited" role="navigation">
<div class="breadcrumbs-container">
<button name="button" type="button" class="toggle-mobile-nav"><span class="sr-only">Open sidebar</span>
<i aria-hidden="true" data-hidden="true" class="fa fa-bars"></i>
</button><div class="breadcrumbs-links js-title-container">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a href="/datasciencedojo">Data Science Dojo</a><svg class="s8 breadcrumbs-list-angle"><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#angle-right"></use></svg></li> <li><a href="/datasciencedojo/tutorials"><img alt="tutorials" class="avatar-tile lazy" width="15" height="15" data-src="/uploads/-/system/project/avatar/80/man-reading.png" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><span class="breadcrumb-item-text js-breadcrumb-item-text">tutorials</span></a><svg class="s8 breadcrumbs-list-angle"><use xlink:href="/assets/icons-2666da8eb968ba69467c0369d020bf011a5d0b1bd253ba0dbcc43bd0ccbd0dcb.svg#angle-right"></use></svg></li>

<li>
<h2 class="breadcrumbs-sub-title"><a href="/datasciencedojo/tutorials/blob/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py">Repository</a></h2>
</li>
</ul>
</div>

</div>
</nav>

<div class="flash-container flash-container-page">
</div>

</div>
<div class=" ">
<div class="content" id="content-body">
<div class="container-fluid container-limited">

<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder">
<form class="project-refs-form" action="/datasciencedojo/tutorials/refs/switch" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="destination" id="destination" value="blob" />
<input type="hidden" name="path" id="path" value="Web Scraping with Python and BeautifulSoup/Web Scraping with Python and Beautiful Soup.py" />
<div class="dropdown">
<button class="dropdown-menu-toggle js-project-refs-dropdown" type="button" data-toggle="dropdown" data-selected="master" data-ref="master" data-refs-url="/datasciencedojo/tutorials/refs?sort=updated_desc" data-field-name="ref" data-submit-form-on-click="true" data-visit="true"><span class="dropdown-toggle-text ">master</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button>
<div class="dropdown-menu dropdown-menu-paging dropdown-menu-selectable git-revision-dropdown">
<div class="dropdown-page-one">
<div class="dropdown-title"><span>Switch branch/tag</span><button class="dropdown-title-button dropdown-menu-close" aria-label="Close" type="button"><i aria-hidden="true" data-hidden="true" class="fa fa-times dropdown-menu-close-icon"></i></button></div>
<div class="dropdown-input"><input type="search" id="" class="dropdown-input-field" placeholder="Search branches and tags" autocomplete="off" /><i aria-hidden="true" data-hidden="true" class="fa fa-search dropdown-input-search"></i><i role="button" aria-hidden="true" data-hidden="true" class="fa fa-times dropdown-input-clear js-dropdown-input-clear"></i></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
</div>
</div>
</form>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li>
<a href="/datasciencedojo/tutorials/tree/master">tutorials
</a></li>
<li>
<a href="/datasciencedojo/tutorials/tree/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup">Web Scraping with Python and Beautifu...</a>
</li>
<li>
<a href="/datasciencedojo/tutorials/blob/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py"><strong>Web Scraping with Python and Beautifu...</strong>
</a></li>
</ul>
</div>
<div class="tree-controls">
<a class="btn shortcuts-find-file" rel="nofollow" href="/datasciencedojo/tutorials/find_file/master"><i aria-hidden="true" data-hidden="true" class="fa fa-search"></i>
<span>Find file</span>
</a>
<div class="btn-group" role="group"><a class="btn js-blob-blame-link" href="/datasciencedojo/tutorials/blame/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py">Blame</a><a class="btn" href="/datasciencedojo/tutorials/commits/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py">History</a><a class="btn js-data-file-blob-permalink-url" href="/datasciencedojo/tutorials/blob/906d4dbc73b47d7af6f725c415896d8fd20b048c/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py">Permalink</a></div>
</div>
</div>

<div class="info-well hidden-xs">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-205f8fa8">
<div class="avatar-cell hidden-xs">
<a href="/arhamakheel"><img alt="Arham Akheel&#39;s avatar" src="https://secure.gravatar.com/avatar/69cecfe07818504c1b991c3c1ec5c69a?s=72&amp;d=identicon" data-container="body" class="avatar s36 hidden-xs has-tooltip" title="Arham Akheel" /></a>
</div>
<div class="commit-detail flex-list">
<div class="commit-content">
<a class="commit-row-message item-title" href="/datasciencedojo/tutorials/commit/205f8fa81c3b0a08b29aba8dd13bf8a767e19f98">Code Changes, last line of Python code</a>
<span class="commit-row-message visible-xs-inline">
&middot;
205f8fa8
</span>
<div class="commiter">
<a class="commit-author-link has-tooltip" title="arham@datasciencedojo.com" href="/arhamakheel">Arham Akheel</a> authored <time class="js-timeago" title="Mar 30, 2018 12:33am" datetime="2018-03-30T00:33:02Z" data-toggle="tooltip" data-placement="bottom" data-container="body">Mar 29, 2018</time>
</div>
</div>
<div class="commit-actions flex-row hidden-xs">

<div class="js-commit-pipeline-status" data-endpoint="/datasciencedojo/tutorials/commit/205f8fa81c3b0a08b29aba8dd13bf8a767e19f98/pipelines"></div>
<a class="commit-sha btn btn-transparent btn-link" href="/datasciencedojo/tutorials/commit/205f8fa81c3b0a08b29aba8dd13bf8a767e19f98">205f8fa8</a>
<button class="btn btn-clipboard btn-transparent" data-toggle="tooltip" data-placement="bottom" data-container="body" data-title="Copy commit SHA to clipboard" data-clipboard-text="205f8fa81c3b0a08b29aba8dd13bf8a767e19f98" type="button" title="Copy commit SHA to clipboard" aria-label="Copy commit SHA to clipboard"><i aria-hidden="true" aria-hidden="true" data-hidden="true" class="fa fa-clipboard"></i></button>

</div>
</div>
</li>

</ul>
</div>

</div>
<div class="blob-content-holder" id="blob-content-holder">
<article class="file-holder">
<div class="js-file-title file-title-flex-parent">
<div class="file-header-content">
<i aria-hidden="true" data-hidden="true" class="fa fa-file-text-o fa-fw"></i>
<strong class="file-title-name">
Web Scraping with Python and Beautiful Soup.py
</strong>
<button class="btn btn-clipboard btn-transparent prepend-left-5" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn-clipboard btn-transparent prepend-left-5" data-title="Copy file path to clipboard" data-clipboard-text="{&quot;text&quot;:&quot;Web Scraping with Python and BeautifulSoup/Web Scraping with Python and Beautiful Soup.py&quot;,&quot;gfm&quot;:&quot;`Web Scraping with Python and BeautifulSoup/Web Scraping with Python and Beautiful Soup.py`&quot;}" type="button" title="Copy file path to clipboard" aria-label="Copy file path to clipboard"><i aria-hidden="true" aria-hidden="true" data-hidden="true" class="fa fa-clipboard"></i></button>
<small>
2.07 KB
</small>
</div>

<div class="file-actions">

<div class="btn-group" role="group"><button class="btn btn btn-sm js-copy-blob-source-btn" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn btn-sm js-copy-blob-source-btn" data-title="Copy source to clipboard" data-clipboard-target=".blob-content[data-blob-id=&#39;0697cbae69837ee06d2eb54415f8e4fb1f5fb50e&#39;]" type="button" title="Copy source to clipboard" aria-label="Copy source to clipboard"><i aria-hidden="true" aria-hidden="true" data-hidden="true" class="fa fa-clipboard"></i></button><a class="btn btn-sm has-tooltip" target="_blank" rel="noopener noreferrer" title="Open raw" data-container="body" href="/datasciencedojo/tutorials/raw/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py"><i aria-hidden="true" data-hidden="true" class="fa fa-file-code-o"></i></a></div>
<div class="btn-group" role="group"><a class="btn js-edit-blob  btn-sm" href="/datasciencedojo/tutorials/edit/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py">Edit</a></div>
</div>
</div>


<div class="blob-viewer" data-type="simple" data-url="/datasciencedojo/tutorials/blob/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py?format=json&amp;viewer=simple">
<div class="text-center prepend-top-default append-bottom-default">
<i aria-hidden="true" aria-label="Loading content…" class="fa fa-spinner fa-spin fa-2x"></i>
</div>

</div>


</article>
</div>

<div class="modal" id="modal-upload-blob">
<div class="modal-dialog modal-lg">
<div class="modal-content">
<div class="modal-header">
<a class="close" data-dismiss="modal" href="#">&times;</a>
<h3 class="page-title">Replace Web Scraping with Python and Beautiful Soup.py</h3>
</div>
<div class="modal-body">
<form class="js-quick-submit js-upload-blob-form form-horizontal" data-method="put" action="/datasciencedojo/tutorials/update/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="JaMjzOfSrHGir1OjlEPVWs2QCGYK2lAGeQYF5SQ0d5BxcSHhKgOxdSqtaHvbMMIoWXvR8yduNFYbzIzVXYVuPQ==" /><div class="dropzone">
<div class="dropzone-previews blob-upload-dropzone-previews">
<p class="dz-message light">
Attach a file by drag &amp; drop or <a class="markdown-selector" href="#">click to upload</a>
</p>
</div>
</div>
<br>
<div class="dropzone-alerts alert alert-danger data" style="display:none"></div>
<div class="form-group commit_message-group">
<label class="control-label" for="commit_message-f07e1e1cc9dade0bbd7bc8668879d855">Commit message
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-f07e1e1cc9dade0bbd7bc8668879d855" class="form-control js-commit-message" placeholder="Replace Web Scraping with Python and Beautiful Soup.py" required="required" rows="3">
Replace Web Scraping with Python and Beautiful Soup.py</textarea>
</div>
</div>
</div>

<input type="hidden" name="branch_name" id="branch_name" />
<input type="hidden" name="create_merge_request" id="create_merge_request" value="1" />
<input type="hidden" name="original_branch" id="original_branch" value="master" class="js-original-branch" />

<div class="form-actions">
<button name="button" type="button" class="btn btn-create btn-upload-file" id="submit-all"><i aria-hidden="true" data-hidden="true" class="fa fa-spin fa-spinner js-loading-icon hidden"></i>
Replace file
</button><a class="btn btn-cancel" data-dismiss="modal" href="#">Cancel</a>
<div class="inline prepend-left-10">
A new branch will be created in your fork and a new merge request will be started.
</div>

</div>
</form></div>
</div>
</div>
</div>

</div>
</div>

</div>
</div>
</div>
</div>


</body>
</html>

