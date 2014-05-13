var curRun;
var editors = {};

function makeCodeMirror(el, runNum)
{
  editors[runNum] = CodeMirror.fromTextArea(el, {
	lineNumbers: true
    //height: "350px"
    //parserfile: "parsexml.js",
    //stylesheet: "css/xmlcolors.css",
    //path: "js/",
    //continuousScanning: 500,
  });
}

$(function() {

  var lang = $("*[data-code-language]").first().attr("data-code-language")
  
  // create textareas from pre, add run buttons
  $("*[data-executable").each(function(i) {
    var txtarea = $("<textarea data-run-number='"+i+"' id='code-run-"+i+"'>" + $(this).text() + "</textarea>");
    var btn = $("<a class='btn run-code-btn run-btn' data-run-number='"+i+"' href='#'>Run Code</a>")
    $(this).after(btn);
    btn.hide();
    $(this).replaceWith(txtarea);
    makeCodeMirror(txtarea[0], i);
  });

  // create jsrepl object
  var jsrepl = new JSREPL({  
    input: function() {},  
    output: function(data) {
      $(".console[data-run-number='"+curRun+"']").append(data);
    },  
    result: function(data) {
      $(".console[data-run-number='"+curRun+"']").append("=> " + data);
    },  
    error: function() {},  
    progress: function() {},  
    timeout: {  
      time: 30000,  
      callback: function() {}  
    }  
  }); 

  // load language
  jsrepl.loadLanguage(lang, function () {

    $(".run-btn").show();

    $(".run-btn").click(function(e) {
      curRun = $(this).attr("data-run-number");
      var pre = $("pre[data-run-number='"+curRun+"'");
      if(pre.length == 0) pre = $("<pre class='console' data-run-number='"+curRun+"'></pre>");
      pre.text("")
      $(this).before(pre);
      jsrepl.eval(editors[curRun].getValue());
      e.preventDefault();
    });

  }); 
});