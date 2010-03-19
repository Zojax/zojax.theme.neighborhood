$(document).ready(function(){
  $("div.z-personalbar-menu a[href*='loginAuth']").click(function (e) {
      e.preventDefault();
      var portal = $('HEAD').attr('portal');
      var form = jQuery.FrameDialog
      .create({
          url: portal + 'modallogin.html',
          buttons:{},
          closeOnEscape: true,
          minWidth:900,
          minHeight:700,
          title: $(this).text()
      });
      form.find('iframe').attr('scrolling', 'no');
      var uid = form.attr('id');
      var interval = window.setInterval(function() {
          var win = window.frames[uid+"-VIEW"];
          var loc = win.location.href;
          if (!loc.match(/login.html/) && !loc.match(/about:blank/) && $("div", win.document).length) {
              $.FrameDialog.setResult(loc, uid);
              $.FrameDialog.closeDialog(uid);
              window.clearInterval(interval)
          }
      }, 250)
      form.bind('dialogclose', function(event, ui) {
          if ($(this).attr('result') && $(this).attr('result') != 'null') {
              window.location.href = $(this).attr('result')
          }
          window.clearInterval(interval)
  });
  })
});
