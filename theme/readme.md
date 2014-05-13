# Atlas Bootstrap Theme

This project shows how to create a basic [Bootstrap](http://getbootstrap.com/) theme for Atlas.

## Local Development

This theme has a simple sinatra app so that you can develop and test your theme locally, which is *wayyyy* better than continually pushing the theme to Atlas for builds.  It uses [Rack::Directory](http://www.ruby-doc.org/gems/docs/e/edgar-rack-1.2.1/Rack/Directory.html) to serve static files from the _theme_ directory, and them mounts the test app as the root ("/").  To start the app:

```
$ bundle install
$ shotgun
```

You can then view the static site at _localhost:9393_.  The cool thing is that this will update as you make changes to the file so that you can see the reults in real time.