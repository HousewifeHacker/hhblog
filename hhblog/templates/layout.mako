<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Housewife Hacker</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- Google Analytics -->
    <script type="text/javascript">

      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-37210283-1']);
      _gaq.push(['_trackPageview']);

      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();

    </script>
    <!-- End Gogle Analytics -->

    <!-- Le styles -->
    <link href="${request.static_url('hiero:static/assets/css/bootstrap.css')}" rel="stylesheet">
    <link href="${request.static_url('hiero:static/assets/css/bootstrap-responsive.css')}" rel="stylesheet">
    <link href="${request.static_url('hhblog:static/codehighlighting.css')}" rel="stylesheet">

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
  </head>

  <body>
    <div>
      <div class="container-fluid">
        <div class="row-fluid">
          <div class="span2">
            &nbsp;
            <!-- this div keeps the content centered -->
          </div>
          <div class="span8">
            <h1 align="center"><a href="${request.route_url('hiero_entry_index')}">housewife_hacker</a></h1>
            <h3 align="center">${'  |  '}
            % for category in categories:
            <a href="${request.route_url('hiero_entry_category', slug=category.slug)}">${category.title}</a>${'  |  '}
              % endfor
            </h3>
            <br><br>
          </div>
        </div>
        <div class="row-fluid">
          <div class="span2">
            &nbsp;
            <!-- this div keeps the content centered -->
          </div>
          <div class="span6">
            ${next.body()}
          </div>
          <div class="span2">
            <!-- the right side bar -->
            <strong>RSS</strong>
              <ul>
                <li><a href="${request.route_url('hiero_entry_rss')}">Entire Blog</a></li>
                % for category in categories:
                  <li><a href="${request.route_url('hiero_entry_rss_category', category=category.title)}">${category.title}</a></li>
                % endfor
              </ul>
            <br>
            <strong>Links</strong>
            <ul>
              <li><a href="https://github.com/HousewifeHacker">My Github</a></li>
              <li><a href="https://live.gnome.org/OutreachProgramForWomen">OPW</a></li>
              <li><a href="https://fedoraproject.org/wiki/User:Ianweller/statistics_plus_plus">Fedora Stats++</a></li>
              <li><a href="http://sontek.net">Blog of Sontek</a></li>
              <li><a href="http://eventray.com">EventRay</a></li>
            </ul>
            <br>
            <a class="twitter-timeline" href="https://twitter.com/housewifehacker" data-widget-id="282244034217508864">Tweets by @housewifehacker</a>
            <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>

          </div>
        </div>
      </div> <!-- /container -->
    </div>

  </body>
</html>
