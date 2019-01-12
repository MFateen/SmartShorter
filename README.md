
<!DOCTYPE html><html><head><meta charset="utf-8"><title>SmartShorter</title><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css"><style>@import url('https://fonts.googleapis.com/css?family=Roboto:400,700|Inconsolata|Raleway:200');.hljs-comment,.hljs-title{color:#8e908c}.hljs-variable,.hljs-attribute,.hljs-tag,.hljs-regexp,.ruby .hljs-constant,.xml .hljs-tag .hljs-title,.xml .hljs-pi,.xml .hljs-doctype,.html .hljs-doctype,.css .hljs-id,.css .hljs-class,.css .hljs-pseudo{color:#c82829}.hljs-number,.hljs-preprocessor,.hljs-pragma,.hljs-built_in,.hljs-literal,.hljs-params,.hljs-constant{color:#f5871f}.ruby .hljs-class .hljs-title,.css .hljs-rules .hljs-attribute{color:#eab700}.hljs-string,.hljs-value,.hljs-inheritance,.hljs-header,.ruby .hljs-symbol,.xml .hljs-cdata{color:#718c00}.css .hljs-hexcolor{color:#3e999f}.hljs-function,.python .hljs-decorator,.python .hljs-title,.ruby .hljs-function .hljs-title,.ruby .hljs-title .hljs-keyword,.perl .hljs-sub,.javascript .hljs-title,.coffeescript .hljs-title{color:#4271ae}.hljs-keyword,.javascript .hljs-function{color:#8959a8}.hljs{display:block;background:white;color:#4d4d4c;padding:.5em}.coffeescript .javascript,.javascript .xml,.tex .hljs-formula,.xml .javascript,.xml .vbscript,.xml .css,.xml .hljs-cdata{opacity:.5}.right .hljs-comment{color:#969896}.right .css .hljs-class,.right .css .hljs-id,.right .css .hljs-pseudo,.right .hljs-attribute,.right .hljs-regexp,.right .hljs-tag,.right .hljs-variable,.right .html .hljs-doctype,.right .ruby .hljs-constant,.right .xml .hljs-doctype,.right .xml .hljs-pi,.right .xml .hljs-tag .hljs-title{color:#c66}.right .hljs-built_in,.right .hljs-constant,.right .hljs-literal,.right .hljs-number,.right .hljs-params,.right .hljs-pragma,.right .hljs-preprocessor{color:#de935f}.right .css .hljs-rule .hljs-attribute,.right .ruby .hljs-class .hljs-title{color:#f0c674}.right .hljs-header,.right .hljs-inheritance,.right .hljs-name,.right .hljs-string,.right .hljs-value,.right .ruby .hljs-symbol,.right .xml .hljs-cdata{color:#b5bd68}.right .css .hljs-hexcolor,.right .hljs-title{color:#8abeb7}.right .coffeescript .hljs-title,.right .hljs-function,.right .javascript .hljs-title,.right .perl .hljs-sub,.right .python .hljs-decorator,.right .python .hljs-title,.right .ruby .hljs-function .hljs-title,.right .ruby .hljs-title .hljs-keyword{color:#81a2be}.right .hljs-keyword,.right .javascript .hljs-function{color:#b294bb}.right .hljs{display:block;overflow-x:auto;background:#1d1f21;color:#c5c8c6;padding:.5em;-webkit-text-size-adjust:none}.right .coffeescript .javascript,.right .javascript .xml,.right .tex .hljs-formula,.right .xml .css,.right .xml .hljs-cdata,.right .xml .javascript,.right .xml .vbscript{opacity:.5}body{color:black;background:white;font:400 14px / 1.42 'Roboto',Helvetica,sans-serif}header{border-bottom:1px solid #f2f2f2;margin-bottom:12px}h1,h2,h3,h4,h5{color:black;margin:12px 0}h1 .permalink,h2 .permalink,h3 .permalink,h4 .permalink,h5 .permalink{margin-left:0;opacity:0;transition:opacity .25s ease}h1:hover .permalink,h2:hover .permalink,h3:hover .permalink,h4:hover .permalink,h5:hover .permalink{opacity:1}.triple h1 .permalink,.triple h2 .permalink,.triple h3 .permalink,.triple h4 .permalink,.triple h5 .permalink{opacity:.15}.triple h1:hover .permalink,.triple h2:hover .permalink,.triple h3:hover .permalink,.triple h4:hover .permalink,.triple h5:hover .permalink{opacity:.15}h1{font:200 36px 'Raleway',Helvetica,sans-serif;font-size:36px}h2{font:200 36px 'Raleway',Helvetica,sans-serif;font-size:30px}h3{font-size:100%;text-transform:uppercase}h5{font-size:100%;font-weight:normal}p{margin:0 0 10px}p.choices{line-height:1.6}a{color:#428bca;text-decoration:none}li p{margin:0}hr.split{border:0;height:1px;width:100%;padding-left:6px;margin:12px auto;background-image:linear-gradient(to right, rgba(0,0,0,0) 20%, rgba(0,0,0,0.2) 51.4%, rgba(255,255,255,0.2) 51.4%, rgba(255,255,255,0) 80%)}dl dt{float:left;width:130px;clear:left;text-align:right;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:700}dl dd{margin-left:150px}blockquote{color:rgba(0,0,0,0.5);font-size:15.5px;padding:10px 20px;margin:12px 0;border-left:5px solid #e8e8e8}blockquote p:last-child{margin-bottom:0}pre{background-color:#f5f5f5;padding:12px;border:1px solid #cfcfcf;border-radius:6px;overflow:auto}pre code{color:black;background-color:transparent;padding:0;border:none}code{color:#444;background-color:#f5f5f5;font:'Inconsolata',monospace;padding:1px 4px;border:1px solid #cfcfcf;border-radius:3px}ul,ol{padding-left:2em}table{border-collapse:collapse;border-spacing:0;margin-bottom:12px}table tr:nth-child(2n){background-color:#fafafa}table th,table td{padding:6px 12px;border:1px solid #e6e6e6}.text-muted{opacity:.5}.note,.warning{padding:.3em 1em;margin:1em 0;border-radius:2px;font-size:90%}.note h1,.warning h1,.note h2,.warning h2,.note h3,.warning h3,.note h4,.warning h4,.note h5,.warning h5,.note h6,.warning h6{font-family:200 36px 'Raleway',Helvetica,sans-serif;font-size:135%;font-weight:500}.note p,.warning p{margin:.5em 0}.note{color:black;background-color:#f0f6fb;border-left:4px solid #428bca}.note h1,.note h2,.note h3,.note h4,.note h5,.note h6{color:#428bca}.warning{color:black;background-color:#fbf1f0;border-left:4px solid #c9302c}.warning h1,.warning h2,.warning h3,.warning h4,.warning h5,.warning h6{color:#c9302c}header{margin-top:24px}nav{position:fixed;top:24px;bottom:0;overflow-y:auto}nav .resource-group{padding:0}nav .resource-group .heading{position:relative}nav .resource-group .heading .chevron{position:absolute;top:12px;right:12px;opacity:.5}nav .resource-group .heading a{display:block;color:black;opacity:.7;border-left:2px solid transparent;margin:0}nav .resource-group .heading a:hover{text-decoration:none;background-color:bad-color;border-left:2px solid black}nav ul{list-style-type:none;padding-left:0}nav ul a{display:block;font-size:13px;color:rgba(0,0,0,0.7);padding:8px 12px;border-top:1px solid #d9d9d9;border-left:2px solid transparent;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}nav ul a:hover{text-decoration:none;background-color:bad-color;border-left:2px solid black}nav ul>li{margin:0}nav ul>li:first-child{margin-top:-12px}nav ul>li:last-child{margin-bottom:-12px}nav ul ul a{padding-left:24px}nav ul ul li{margin:0}nav ul ul li:first-child{margin-top:0}nav ul ul li:last-child{margin-bottom:0}nav>div>div>ul>li:first-child>a{border-top:none}.preload *{transition:none !important}.pull-left{float:left}.pull-right{float:right}.badge{display:inline-block;float:right;min-width:10px;min-height:14px;padding:3px 7px;font-size:12px;color:#000;background-color:#f2f2f2;border-radius:10px;margin:-2px 0}.badge.get{color:#70bbe1;background-color:#d9edf7}.badge.head{color:#70bbe1;background-color:#d9edf7}.badge.options{color:#70bbe1;background-color:#d9edf7}.badge.put{color:#f0db70;background-color:#fcf8e3}.badge.patch{color:#f0db70;background-color:#fcf8e3}.badge.post{color:#93cd7c;background-color:#dff0d8}.badge.delete{color:#ce8383;background-color:#f2dede}.collapse-button{float:right}.collapse-button .close{display:none;color:#428bca;cursor:pointer}.collapse-button .open{color:#428bca;cursor:pointer}.collapse-button.show .close{display:inline}.collapse-button.show .open{display:none}.collapse-content{max-height:0;overflow:hidden;transition:max-height .3s ease-in-out}nav{width:220px}.container{max-width:940px;margin-left:auto;margin-right:auto}.container .row .content{margin-left:244px;width:696px}.container .row:after{content:'';display:block;clear:both}.container-fluid nav{width:22%}.container-fluid .row .content{margin-left:24%}.container-fluid.triple nav{width:16.5%;padding-right:1px}.container-fluid.triple .row .content{position:relative;margin-left:16.5%;padding-left:24px}.middle:before,.middle:after{content:'';display:table}.middle:after{clear:both}.middle{box-sizing:border-box;width:51.5%;padding-right:12px}.right{box-sizing:border-box;float:right;width:48.5%;padding-left:12px}.right a{color:#428bca}.right h1,.right h2,.right h3,.right h4,.right h5,.right p,.right div{color:white}.right pre{background-color:#1d1f21;border:1px solid #1d1f21}.right pre code{color:#c5c8c6}.right .description{margin-top:12px}.triple .resource-heading{font-size:125%}.definition{margin-top:12px;margin-bottom:12px}.definition .method{font-weight:bold}.definition .method.get{color:#2e8ab8}.definition .method.head{color:#2e8ab8}.definition .method.options{color:#2e8ab8}.definition .method.post{color:#56b82e}.definition .method.put{color:#b8a22e}.definition .method.patch{color:#b8a22e}.definition .method.delete{color:#b82e2e}.definition .uri{word-break:break-all;word-wrap:break-word}.definition .hostname{opacity:.5}.example-names{background-color:#eee;padding:12px;border-radius:6px}.example-names .tab-button{cursor:pointer;color:black;border:1px solid #ddd;padding:6px;margin-left:12px}.example-names .tab-button.active{background-color:#d5d5d5}.right .example-names{background-color:#444}.right .example-names .tab-button{color:white;border:1px solid #666;border-radius:6px}.right .example-names .tab-button.active{background-color:#5e5e5e}#nav-background{position:fixed;left:0;top:0;bottom:0;width:16.5%;padding-right:14.4px;background-color:#fbfbfb;border-right:1px solid #f0f0f0;z-index:-1}#right-panel-background{position:absolute;right:-12px;top:-12px;bottom:-12px;width:48.6%;background-color:#333;z-index:-1}@media (max-width:1200px){nav{width:198px}.container{max-width:840px}.container .row .content{margin-left:224px;width:606px}}@media (max-width:992px){nav{width:169.4px}.container{max-width:720px}.container .row .content{margin-left:194px;width:526px}}@media (max-width:768px){nav{display:none}.container{width:95%;max-width:none}.container .row .content,.container-fluid .row .content,.container-fluid.triple .row .content{margin-left:auto;margin-right:auto;width:95%}#nav-background{display:none}#right-panel-background{width:48.6%}}.back-to-top{position:fixed;z-index:1;bottom:0;right:24px;padding:4px 8px;color:rgba(0,0,0,0.5);background-color:#f2f2f2;text-decoration:none !important;border-top:1px solid #d9d9d9;border-left:1px solid #d9d9d9;border-right:1px solid #d9d9d9;border-top-left-radius:3px;border-top-right-radius:3px}.resource-group{padding:12px;margin-bottom:12px;background-color:white;border:1px solid #d9d9d9;border-radius:6px}.resource-group h2.group-heading,.resource-group .heading a{padding:12px;margin:-12px -12px 12px -12px;background-color:#f2f2f2;border-bottom:1px solid #d9d9d9;border-top-left-radius:6px;border-top-right-radius:6px;white-space:nowrap;text-overflow:ellipsis;overflow:hidden}.triple .content .resource-group{padding:0;border:none}.triple .content .resource-group h2.group-heading,.triple .content .resource-group .heading a{margin:0 0 12px 0;border:1px solid #d9d9d9}nav .resource-group .heading a{padding:12px;margin-bottom:0}nav .resource-group .collapse-content{padding:0}.action{margin-bottom:12px;padding:12px 12px 0 12px;overflow:hidden;border:1px solid transparent;border-radius:6px}.action h4.action-heading{padding:12px;margin:-12px -12px 12px -12px;border-bottom:1px solid transparent;border-top-left-radius:6px;border-top-right-radius:6px;white-space:nowrap;text-overflow:ellipsis;overflow:hidden}.action h4.action-heading .name{float:right;font-weight:normal}.action h4.action-heading .method{padding:6px 12px;margin-right:12px;border-radius:3px}.action h4.action-heading .method.get{color:#fff;background-color:#337ab7}.action h4.action-heading .method.head{color:#fff;background-color:#337ab7}.action h4.action-heading .method.options{color:#fff;background-color:#337ab7}.action h4.action-heading .method.put{color:#fff;background-color:#ed9c28}.action h4.action-heading .method.patch{color:#fff;background-color:#ed9c28}.action h4.action-heading .method.post{color:#fff;background-color:#5cb85c}.action h4.action-heading .method.delete{color:#fff;background-color:#d9534f}.action h4.action-heading code{color:#444;background-color:#f5f5f5;border-color:#cfcfcf;font-weight:normal}.action dl.inner{padding-bottom:2px}.action .title{border-bottom:1px solid white;margin:0 -12px -1px -12px;padding:12px}.action.get{border-color:#bce8f1}.action.get h4.action-heading{color:#337ab7;background:#d9edf7;border-bottom-color:#bce8f1}.action.head{border-color:#bce8f1}.action.head h4.action-heading{color:#337ab7;background:#d9edf7;border-bottom-color:#bce8f1}.action.options{border-color:#bce8f1}.action.options h4.action-heading{color:#337ab7;background:#d9edf7;border-bottom-color:#bce8f1}.action.post{border-color:#d6e9c6}.action.post h4.action-heading{color:#5cb85c;background:#dff0d8;border-bottom-color:#d6e9c6}.action.put{border-color:#faebcc}.action.put h4.action-heading{color:#ed9c28;background:#fcf8e3;border-bottom-color:#faebcc}.action.patch{border-color:#faebcc}.action.patch h4.action-heading{color:#ed9c28;background:#fcf8e3;border-bottom-color:#faebcc}.action.delete{border-color:#ebccd1}.action.delete h4.action-heading{color:#d9534f;background:#f2dede;border-bottom-color:#ebccd1}</style></head><body class="preload"><a href="#top" class="text-muted back-to-top"><i class="fa fa-toggle-up"></i>&nbsp;Back to top</a><div class="container"><div class="row"><nav><div class="resource-group"><div class="heading"><div class="chevron"><i class="open fa fa-angle-down"></i></div><a href="#top">Overview</a></div><div class="collapse-content"><ul><li><a href="#header-overview">Overview</a></li><li><a href="#header-task">Task</a></li><li><a href="#header-requirement">Requirement</a></li><li><a href="#header-tips">Tips</a></li><li><a href="#header-bonuses">Bonuses</a></li><li><a href="#header-references">References</a></li><li><a href="#header-data-schema">Data Schema</a></li><li><a href="#header-short-link-schema">Short Link Schema</a></li></ul></div></div><div class="resource-group"><div class="heading"><div class="chevron"><i class="open fa fa-angle-down"></i></div><a href="#shortlink-api">shortlink API</a></div><div class="collapse-content"><ul><li><a href="#shortlink-api-shortlinks">Shortlinks</a><ul><li><a href="#shortlink-api-shortlinks-get"><span class="badge get"><i class="fa fa-arrow-down"></i></span>List All Shortlinks</a></li><li><a href="#shortlink-api-shortlinks-post"><span class="badge post"><i class="fa fa-plus"></i></span>Create Shortlink</a></li></ul></li><li><a href="#shortlink-api-shortlink-put"><span class="badge put"><i class="fa fa-pencil"></i></span>Update Link Data</a></li></ul></div></div><p style="text-align: center; word-wrap: break-word;"><a href="127.0.0.1:5000">127.0.0.1:5000</a></p></nav><div class="content"><header><h1 id="top">SmartShorter</h1></header><blockquote>
<p>Smart Link Shortener REST API</p>
</blockquote>
<p><strong><em>This a Test Task to Assess Your Coding and learning Skills.</em></strong></p>
<h2 id="header-overview">Overview <a class="permalink" href="#header-overview" aria-hidden="true">¶</a></h2>
<p>the task is to implement a simple api for smart link shortener service,
a link shortener service like <code>bit.ly</code>, <code>goo.gl</code> and many others. with different
redirection ‘destination’ URL/Link based on the users platform for example
if the short link if a short link is opened for desktop web browser it will redirect
to one location but if open for mobile Android for have a different location.</p>
<p>Imagine a App with download link when open from iOS it opens the page for the iOS app
if from Android it opens the Android app download page, …etc</p>
<h2 id="header-task">Task <a class="permalink" href="#header-task" aria-hidden="true">¶</a></h2>
<p>Implement a RESTful API for the shortlinks as documented below,
<em>not HTML or web design</em> only <em>JSON</em> requests and responds. With no user authentication
the API will be single user/open for all to read/write any link. Implementing user
authentication is a bonus (<em>basicAuth or OAuth2</em>)</p>
<div class="warning">
<h3 id="header-requirement">Requirement <a class="permalink" href="#header-requirement" aria-hidden="true">¶</a></h3>
<ul>
<li>
<p>Use Python 3.5</p>
</li>
<li>
<p>Use <a href="http://flask.pocoo.org/">Flask 0.11</a> web framework</p>
</li>
<li>
<p>Use <a href="https://api.mongodb.com/python/current/">PyMongo</a> (<em>don’t use flask-pymongo</em>)</p>
</li>
<li>
<p>Use <a href="https://git-scm.com">git</a></p>
<ul>
<li>git commit log is required <strong>write good commit log</strong></li>
<li>the task should be posted to <a href="https://gitlab.com">Gitlab</a>/Github and send the link</li>
</ul>
</li>
<li>
<p>Implement the API as documented below</p>
</li>
<li>
<p>MVC, separate logic form representation,</p>
</li>
<li>
<p>Use flask blueprint or app object.</p>
</li>
</ul>
</div>
<div class="note">
<h3 id="header-tips">Tips <a class="permalink" href="#header-tips" aria-hidden="true">¶</a></h3>
<ul>
<li>
<p>Use <a href="http://mongoframes.com/">mongoFrames</a>.</p>
</li>
<li>
<p>Implement/use decorators when ever possible.</p>
</li>
<li>
<p>Use Comprehensions when clear and simple</p>
</li>
<li>
<p>Use <code>simplejson</code> with support for <code>for_json()</code></p>
</li>
</ul>
</div>
<div class="note">
<h3 id="header-bonuses">Bonuses <a class="permalink" href="#header-bonuses" aria-hidden="true">¶</a></h3>
<ul>
<li>
<p>unittest</p>
</li>
<li>
<p>Show you skills 💪</p>
</li>
</ul>
</div>
<div class="note">
<h3 id="header-references">References <a class="permalink" href="#header-references" aria-hidden="true">¶</a></h3>
<p><strong>📚 Flask</strong>:</p>
<ul>
<li>
<p><a href="http://flask.pocoo.org/docs/0.10/tutorial/#tutorial">flask tutorial [Recommended]</a></p>
</li>
<li>
<p><a href="https://exploreflask.com/en/latest/">explore flask</a></p>
</li>
<li>
<p><a href="http://flask.pocoo.org/extensions/">flask extensions</a></p>
</li>
<li>
<p><a href="http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world">the flask mega tutorial [Recommended] </a></p>
</li>
<li>
<p><a href="http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_RESTAPI_with_Flask.php">Python MongoDB RESTAPI with Flask tutorial</a></p>
</li>
<li>
<p>Flask Video tutorial [Recommended]</p>
<ul>
<li><a href="http://pyvideo.org/video/2608/flask-by-example">http://pyvideo.org/video/2608/flask-by-example</a></li>
<li><a href="http://pyvideo.org/video/3410/flask-workshop">http://pyvideo.org/video/3410/flask-workshop</a></li>
<li><a href="http://pyvideo.org/video/2668/writing-restful-web-services-with-flask">http://pyvideo.org/video/2668/writing-restful-web-services-with-flask</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="header-data-schema">Data Schema <a class="permalink" href="#header-data-schema" aria-hidden="true">¶</a></h2>
<h3 id="header-short-link-schema">Short Link Schema <a class="permalink" href="#header-short-link-schema" aria-hidden="true">¶</a></h3>
<pre><code><span class="hljs-attribute">slug</span>: <span class="hljs-string">"s5G1f3"</span>
<span class="hljs-attribute">ios</span>:
  <span class="hljs-attribute">primary</span>: <span class="hljs-string">"http://..."</span>
  <span class="hljs-attribute">fallback</span>: <span class="hljs-string">"http://..."</span>
<span class="hljs-attribute">android</span>:
  <span class="hljs-attribute">primary</span>: <span class="hljs-string">"http://..."</span>
  <span class="hljs-attribute">fallback</span>: <span class="hljs-string">"http://..."</span>
<span class="hljs-attribute">web</span>: <span class="hljs-string">"http://..."</span></code></pre>
<section id="shortlink-api" class="resource-group"><h2 class="group-heading">shortlink API <a href="#shortlink-api" class="permalink">&para;</a></h2><div id="shortlink-api-shortlinks" class="resource"><h3 class="resource-heading">Shortlinks <a href="#shortlink-api-shortlinks" class="permalink">&nbsp;&para;</a></h3><div id="shortlink-api-shortlinks-get" class="action get"><h4 class="action-heading"><div class="name">List All Shortlinks</div><a href="#shortlink-api-shortlinks-get" class="method get">GET</a><code class="uri">/shortlinks</code></h4><p>Return List of All User’s Short Links
return empty list if have no link</p>
<h4>Example URI</h4><div class="definition"><span class="method get">GET</span>&nbsp;<span class="uri"><span class="hostname">127.0.0.1:5000</span>/shortlinks</span></div><div class="title"><strong>Request&nbsp;&nbsp;<code>&quot;List Shortlinks&quot;</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>200</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">shortlinks</span>": <span class="hljs-value">[
    {
      "<span class="hljs-attribute">slug</span>": <span class="hljs-value"><span class="hljs-string">"s5G1f3"</span></span>,
      "<span class="hljs-attribute">ios</span>": <span class="hljs-value">{
        "<span class="hljs-attribute">primary</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span></span>,
        "<span class="hljs-attribute">fallback</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
      </span>}</span>,
      "<span class="hljs-attribute">android</span>": <span class="hljs-value">{
        "<span class="hljs-attribute">primary</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span></span>,
        "<span class="hljs-attribute">fallback</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
      </span>}</span>,
      "<span class="hljs-attribute">web</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
    </span>},
    {
      "<span class="hljs-attribute">slug</span>": <span class="hljs-value"><span class="hljs-string">"s5G1f3"</span></span>,
      "<span class="hljs-attribute">ios</span>": <span class="hljs-value">{
        "<span class="hljs-attribute">primary</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span></span>,
        "<span class="hljs-attribute">fallback</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
      </span>}</span>,
      "<span class="hljs-attribute">android</span>": <span class="hljs-value">{
        "<span class="hljs-attribute">primary</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span></span>,
        "<span class="hljs-attribute">fallback</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
      </span>}</span>,
      "<span class="hljs-attribute">web</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
    </span>},
    {
      "<span class="hljs-attribute">slug</span>": <span class="hljs-value"><span class="hljs-string">"s5G1f3"</span></span>,
      "<span class="hljs-attribute">ios</span>": <span class="hljs-value">{
        "<span class="hljs-attribute">primary</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span></span>,
        "<span class="hljs-attribute">fallback</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
      </span>}</span>,
      "<span class="hljs-attribute">android</span>": <span class="hljs-value">{
        "<span class="hljs-attribute">primary</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span></span>,
        "<span class="hljs-attribute">fallback</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
      </span>}</span>,
      "<span class="hljs-attribute">web</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
    </span>}
  ]
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">shortlinks</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"array"</span>
    </span>}
  </span>}</span>,
  "<span class="hljs-attribute">required</span>": <span class="hljs-value">[
    <span class="hljs-string">"shortlinks"</span>
  ]
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>404</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"failed"</span></span>,
  "<span class="hljs-attribute">message</span>": <span class="hljs-value"><span class="hljs-string">"not found"</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">status</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">message</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>401</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><div class="description"><div class="warning">
<p><strong>NOT REQUIRED</strong> <em>if implementing multiple user with user auth only</em></p>
</div>
</div><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"failed"</span></span>,
  "<span class="hljs-attribute">message</span>": <span class="hljs-value"><span class="hljs-string">"auth failed, failed to login user"</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">status</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">message</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>500</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Request&nbsp;&nbsp;<code>&quot;Case Non-JSON Content-Type&quot;</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">text/html</span></code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>400</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"failed"</span></span>,
  "<span class="hljs-attribute">message</span>": <span class="hljs-value"><span class="hljs-string">"Bad Request"</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">status</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">message</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div></div><div id="shortlink-api-shortlinks-post" class="action post"><h4 class="action-heading"><div class="name">Create Shortlink</div><a href="#shortlink-api-shortlinks-post" class="method post">POST</a><code class="uri">/shortlinks</code></h4><p>Create New shortlink,</p>
<p>the JSON requrest below  require all targts(ios,android,web) to be sent to create a new shortlink
while <code>slug</code> is optional it will be genrated if not sent with the requrest
this to allow for roundome alphanumiric shortlink and custome shortlink if <code>slug</code>
was sent.</p>
<div class="note">
<h4 id="header-note">NOTE <a class="permalink" href="#header-note" aria-hidden="true">¶</a></h4>
<p><strong>for the backend</strong></p>
<ul>
<li>
<p>the <code>slug</code> should be unique provided or auto generated</p>
</li>
<li>
<p>the <code>slug</code> is an case-sensitive alphanumeric</p>
</li>
</ul>
</div>
<h4>Example URI</h4><div class="definition"><span class="method post">POST</span>&nbsp;<span class="uri"><span class="hostname">127.0.0.1:5000</span>/shortlinks</span></div><div class="title"><strong>Request&nbsp;&nbsp;<code>&quot;Create Shortlink&quot;</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">slug</span>": <span class="hljs-value"><span class="hljs-string">"s5G1f3"</span></span>,
  "<span class="hljs-attribute">ios</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">primary</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span></span>,
    "<span class="hljs-attribute">fallback</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
  </span>}</span>,
  "<span class="hljs-attribute">android</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">primary</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span></span>,
    "<span class="hljs-attribute">fallback</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
  </span>}</span>,
  "<span class="hljs-attribute">web</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">slug</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span></span>,
      "<span class="hljs-attribute">description</span>": <span class="hljs-value"><span class="hljs-string">"shortlink code"</span>
    </span>}</span>,
    "<span class="hljs-attribute">ios</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
      "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
        "<span class="hljs-attribute">primary</span>": <span class="hljs-value">{
          "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
        </span>}</span>,
        "<span class="hljs-attribute">fallback</span>": <span class="hljs-value">{
          "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
        </span>}
      </span>}</span>,
      "<span class="hljs-attribute">required</span>": <span class="hljs-value">[
        <span class="hljs-string">"primary"</span>,
        <span class="hljs-string">"fallback"</span>
      ]</span>,
      "<span class="hljs-attribute">description</span>": <span class="hljs-value"><span class="hljs-string">"iPhone URLs"</span>
    </span>}</span>,
    "<span class="hljs-attribute">android</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
      "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
        "<span class="hljs-attribute">primary</span>": <span class="hljs-value">{
          "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
        </span>}</span>,
        "<span class="hljs-attribute">fallback</span>": <span class="hljs-value">{
          "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
        </span>}
      </span>}</span>,
      "<span class="hljs-attribute">required</span>": <span class="hljs-value">[
        <span class="hljs-string">"primary"</span>,
        <span class="hljs-string">"fallback"</span>
      ]</span>,
      "<span class="hljs-attribute">description</span>": <span class="hljs-value"><span class="hljs-string">"Android URLs"</span>
    </span>}</span>,
    "<span class="hljs-attribute">web</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span></span>,
      "<span class="hljs-attribute">description</span>": <span class="hljs-value"><span class="hljs-string">"Other platforms"</span>
    </span>}
  </span>}</span>,
  "<span class="hljs-attribute">required</span>": <span class="hljs-value">[
    <span class="hljs-string">"ios"</span>,
    <span class="hljs-string">"android"</span>,
    <span class="hljs-string">"web"</span>
  ]
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>201</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><div class="description"><div class="note">
<h4 id="header-note-1">NOTE <a class="permalink" href="#header-note-1" aria-hidden="true">¶</a></h4>
<p>return generated <code>slug</code></p>
</div>
</div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"successful"</span></span>,
  "<span class="hljs-attribute">slug</span>": <span class="hljs-value"><span class="hljs-string">"s5G1f3"</span></span>,
  "<span class="hljs-attribute">message</span>": <span class="hljs-value"><span class="hljs-string">"created successfully"</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">status</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">slug</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">message</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>404</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"failed"</span></span>,
  "<span class="hljs-attribute">message</span>": <span class="hljs-value"><span class="hljs-string">"not found"</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">status</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">message</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>401</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><div class="description"><div class="warning">
<p><strong>NOT REQUIRED</strong> <em>if implementing multiple user with user auth only</em></p>
</div>
</div><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"failed"</span></span>,
  "<span class="hljs-attribute">message</span>": <span class="hljs-value"><span class="hljs-string">"auth failed, failed to login user"</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">status</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">message</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>500</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Request&nbsp;&nbsp;<code>&quot;Case Non-JSON Content-Type&quot;</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">text/html</span></code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>400</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"failed"</span></span>,
  "<span class="hljs-attribute">message</span>": <span class="hljs-value"><span class="hljs-string">"Bad Request"</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">status</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">message</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div></div></div><div id="shortlink-api-shortlink" class="resource"><h3 class="resource-heading">shortlink <a href="#shortlink-api-shortlink" class="permalink">&nbsp;&para;</a></h3><div id="shortlink-api-shortlink-put" class="action put"><h4 class="action-heading"><div class="name">Update Link Data</div><a href="#shortlink-api-shortlink-put" class="method put">PUT</a><code class="uri">/shortlinks/{slug}</code></h4><div class="note">
<h4 id="header-note-2">NOTE <a class="permalink" href="#header-note-2" aria-hidden="true">¶</a></h4>
<p>the <code>slug</code> is readonly once it’s been created,
this means it can’t be update.</p>
</div>
<p>Only sent attr will be updated, other will stay as is</p>
<h4>Example URI</h4><div class="definition"><span class="method put">PUT</span>&nbsp;<span class="uri"><span class="hostname">127.0.0.1:5000</span>/shortlinks/<span class="hljs-attribute" title="slug">s5G1f3</span></span></div><div class="title"><strong>URI Parameters</strong><div class="collapse-button show"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><dl class="inner"><dt>slug</dt><dd><code>string</code>&nbsp;<span class="required">(required)</span>&nbsp;<span class="text-muted example"><strong>Example:&nbsp;</strong><span>s5G1f3</span></span><p>alphanumeric Shortlink code</p>
</dd></dl></div><div class="title"><strong>Request&nbsp;&nbsp;<code>&quot;ex: update iOS fallback only&quot;</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">ios</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">fallback</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
  </span>}
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">ios</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
      "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
        "<span class="hljs-attribute">fallback</span>": <span class="hljs-value">{
          "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
        </span>}
      </span>}</span>,
      "<span class="hljs-attribute">description</span>": <span class="hljs-value"><span class="hljs-string">"iPhone URLs"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Request&nbsp;&nbsp;<code>&quot;ex: update web only&quot;</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">web</span>": <span class="hljs-value"><span class="hljs-string">"http://..."</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">web</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span></span>,
      "<span class="hljs-attribute">description</span>": <span class="hljs-value"><span class="hljs-string">"Other platforms"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>201</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"successful"</span></span>,
  "<span class="hljs-attribute">message</span>": <span class="hljs-value"><span class="hljs-string">"updated successfully"</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">status</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">message</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>404</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"failed"</span></span>,
  "<span class="hljs-attribute">message</span>": <span class="hljs-value"><span class="hljs-string">"not found"</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">status</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">message</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>401</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><div class="description"><div class="warning">
<p><strong>NOT REQUIRED</strong> <em>if implementing multiple user with user auth only</em></p>
</div>
</div><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"failed"</span></span>,
  "<span class="hljs-attribute">message</span>": <span class="hljs-value"><span class="hljs-string">"auth failed, failed to login user"</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">status</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">message</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Request&nbsp;&nbsp;<code>&quot;Case Non-JSON Content-Type&quot;</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">text/html</span></code></pre><div style="height: 1px;"></div></div></div><div class="title"><strong>Response&nbsp;&nbsp;<code>400</code></strong><div class="collapse-button"><span class="close">Hide</span><span class="open">Show</span></div></div><div class="collapse-content"><div class="inner"><h5>Headers</h5><pre><code><span class="hljs-attribute">Content-Type</span>: <span class="hljs-string">application/json</span></code></pre><div style="height: 1px;"></div><h5>Body</h5><pre><code>{
  "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"failed"</span></span>,
  "<span class="hljs-attribute">message</span>": <span class="hljs-value"><span class="hljs-string">"Bad Request"</span>
</span>}</code></pre><div style="height: 1px;"></div><h5>Schema</h5><pre><code>{
  "<span class="hljs-attribute">$schema</span>": <span class="hljs-value"><span class="hljs-string">"http://json-schema.org/draft-04/schema#"</span></span>,
  "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"object"</span></span>,
  "<span class="hljs-attribute">properties</span>": <span class="hljs-value">{
    "<span class="hljs-attribute">status</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}</span>,
    "<span class="hljs-attribute">message</span>": <span class="hljs-value">{
      "<span class="hljs-attribute">type</span>": <span class="hljs-value"><span class="hljs-string">"string"</span>
    </span>}
  </span>}
</span>}</code></pre><div style="height: 1px;"></div></div></div></div></div></section></div></div></div><p style="text-align: center;" class="text-muted">Generated by&nbsp;<a href="https://github.com/danielgtaylor/aglio" class="aglio">aglio</a>&nbsp;on 07 Aug 2016</p><script>/* eslint-env browser */
/* eslint quotes: [2, "single"] */
'use strict';

/*
  Determine if a string ends with another string.
*/
function endsWith(str, suffix) {
    return str.indexOf(suffix, str.length - suffix.length) !== -1;
}

/*
  Get a list of direct child elements by class name.
*/
function childrenByClass(element, name) {
  var filtered = [];

  for (var i = 0; i < element.children.length; i++) {
    var child = element.children[i];
    var classNames = child.className.split(' ');
    if (classNames.indexOf(name) !== -1) {
      filtered.push(child);
    }
  }

  return filtered;
}

/*
  Get an array [width, height] of the window.
*/
function getWindowDimensions() {
  var w = window,
      d = document,
      e = d.documentElement,
      g = d.body,
      x = w.innerWidth || e.clientWidth || g.clientWidth,
      y = w.innerHeight || e.clientHeight || g.clientHeight;

  return [x, y];
}

/*
  Collapse or show a request/response example.
*/
function toggleCollapseButton(event) {
    var button = event.target.parentNode;
    var content = button.parentNode.nextSibling;
    var inner = content.children[0];

    if (button.className.indexOf('collapse-button') === -1) {
      // Clicked without hitting the right element?
      return;
    }

    if (content.style.maxHeight && content.style.maxHeight !== '0px') {
        // Currently showing, so let's hide it
        button.className = 'collapse-button';
        content.style.maxHeight = '0px';
    } else {
        // Currently hidden, so let's show it
        button.className = 'collapse-button show';
        content.style.maxHeight = inner.offsetHeight + 12 + 'px';
    }
}

function toggleTabButton(event) {
    var i, index;
    var button = event.target;

    // Get index of the current button.
    var buttons = childrenByClass(button.parentNode, 'tab-button');
    for (i = 0; i < buttons.length; i++) {
        if (buttons[i] === button) {
            index = i;
            button.className = 'tab-button active';
        } else {
            buttons[i].className = 'tab-button';
        }
    }

    // Hide other tabs and show this one.
    var tabs = childrenByClass(button.parentNode.parentNode, 'tab');
    for (i = 0; i < tabs.length; i++) {
        if (i === index) {
            tabs[i].style.display = 'block';
        } else {
            tabs[i].style.display = 'none';
        }
    }
}

/*
  Collapse or show a navigation menu. It will not be hidden unless it
  is currently selected or `force` has been passed.
*/
function toggleCollapseNav(event, force) {
    var heading = event.target.parentNode;
    var content = heading.nextSibling;
    var inner = content.children[0];

    if (heading.className.indexOf('heading') === -1) {
      // Clicked without hitting the right element?
      return;
    }

    if (content.style.maxHeight && content.style.maxHeight !== '0px') {
      // Currently showing, so let's hide it, but only if this nav item
      // is already selected. This prevents newly selected items from
      // collapsing in an annoying fashion.
      if (force || window.location.hash && endsWith(event.target.href, window.location.hash)) {
        content.style.maxHeight = '0px';
      }
    } else {
      // Currently hidden, so let's show it
      content.style.maxHeight = inner.offsetHeight + 12 + 'px';
    }
}

/*
  Refresh the page after a live update from the server. This only
  works in live preview mode (using the `--server` parameter).
*/
function refresh(body) {
    document.querySelector('body').className = 'preload';
    document.body.innerHTML = body;

    // Re-initialize the page
    init();
    autoCollapse();

    document.querySelector('body').className = '';
}

/*
  Determine which navigation items should be auto-collapsed to show as many
  as possible on the screen, based on the current window height. This also
  collapses them.
*/
function autoCollapse() {
  var windowHeight = getWindowDimensions()[1];
  var itemsHeight = 64; /* Account for some padding */
  var itemsArray = Array.prototype.slice.call(
    document.querySelectorAll('nav .resource-group .heading'));

  // Get the total height of the navigation items
  itemsArray.forEach(function (item) {
    itemsHeight += item.parentNode.offsetHeight;
  });

  // Should we auto-collapse any nav items? Try to find the smallest item
  // that can be collapsed to show all items on the screen. If not possible,
  // then collapse the largest item and do it again. First, sort the items
  // by height from smallest to largest.
  var sortedItems = itemsArray.sort(function (a, b) {
    return a.parentNode.offsetHeight - b.parentNode.offsetHeight;
  });

  while (sortedItems.length && itemsHeight > windowHeight) {
    for (var i = 0; i < sortedItems.length; i++) {
      // Will collapsing this item help?
      var itemHeight = sortedItems[i].nextSibling.offsetHeight;
      if ((itemsHeight - itemHeight <= windowHeight) || i === sortedItems.length - 1) {
        // It will, so let's collapse it, remove its content height from
        // our total and then remove it from our list of candidates
        // that can be collapsed.
        itemsHeight -= itemHeight;
        toggleCollapseNav({target: sortedItems[i].children[0]}, true);
        sortedItems.splice(i, 1);
        break;
      }
    }
  }
}

/*
  Initialize the interactive functionality of the page.
*/
function init() {
    var i, j;

    // Make collapse buttons clickable
    var buttons = document.querySelectorAll('.collapse-button');
    for (i = 0; i < buttons.length; i++) {
        buttons[i].onclick = toggleCollapseButton;

        // Show by default? Then toggle now.
        if (buttons[i].className.indexOf('show') !== -1) {
            toggleCollapseButton({target: buttons[i].children[0]});
        }
    }

    var responseCodes = document.querySelectorAll('.example-names');
    for (i = 0; i < responseCodes.length; i++) {
        var tabButtons = childrenByClass(responseCodes[i], 'tab-button');
        for (j = 0; j < tabButtons.length; j++) {
            tabButtons[j].onclick = toggleTabButton;

            // Show by default?
            if (j === 0) {
                toggleTabButton({target: tabButtons[j]});
            }
        }
    }

    // Make nav items clickable to collapse/expand their content.
    var navItems = document.querySelectorAll('nav .resource-group .heading');
    for (i = 0; i < navItems.length; i++) {
        navItems[i].onclick = toggleCollapseNav;

        // Show all by default
        toggleCollapseNav({target: navItems[i].children[0]});
    }
}

// Initial call to set up buttons
init();

window.onload = function () {
    autoCollapse();
    // Remove the `preload` class to enable animations
    document.querySelector('body').className = '';
};
</script></body></html>