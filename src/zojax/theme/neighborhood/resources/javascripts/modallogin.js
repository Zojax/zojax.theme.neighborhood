$(document).ready(function(){
  $("div.z-personalbar-menu a[href*='loginAuth']").click(function (e) {
      e.preventDefault();
      var portal = $('HEAD').attr('portal');
      var form = jQuery.FrameDialog
      .create({
          url: portal + 'modallogin.html',
          buttons:{},
          closeOnEscape: true,
          minWidth:800,
          minHeight:600,
          title: $(this).text(),
      });
      form.find('iframe').attr('scrolling', 'no');
      var uid = form.attr('id');
      var interval = window.setInterval(function() {
          var win = window.frames[uid+"-VIEW"];
          var loc = win.location.href;
          if (!loc.match(/login.html/) && !loc.match(/about:blank/) && $(win).find("div").length) {
              $.FrameDialog.setResult(loc, uid);
              $.FrameDialog.closeDialog(uid);
              window.clearInterval(interval)
          }
      }, 1000)
      form.bind('dialogclose', function(event, ui) {
          if ($(this).attr('result'))
              window.location.href = $(this).attr('result')
  });
  })
});
