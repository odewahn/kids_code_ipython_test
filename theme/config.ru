require './app.rb'
require 'rack'


# With this method of creating a URL Map, instantiate apps using the new method
run Rack::URLMap.new({
  "/theme"  => Rack::Directory.new("theme"),
  "/"   => App.new
})



