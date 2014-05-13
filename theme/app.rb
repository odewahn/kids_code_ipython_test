require 'sinatra'
require 'liquid'


class App < Sinatra::Base

  get "/" do

    atlas_data = {
      'title' => "Bootstrap theme test",
      'doctype' => "<html lang='en' xmlns='http://www.w3.org/1999/xhtml'>",
      'content' => IO.read("sample-content.html"),
      'toc' => IO.read("sample-toc.html"),
      'prev_link' => "Previous",
      'next_link' => "Next"
    }

    @template = Liquid::Template.parse(IO.read("theme/html/layout.html"))
    @template.render(atlas_data)
    
  end
  
end