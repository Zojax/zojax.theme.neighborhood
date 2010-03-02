$(document).ready(function(){
  $("div.z-personalbar-menu a[href*='loginAuth']").click(function (e) {
      e.preventDefault();
      var portal = $('HEAD').attr('portal');
      var form = $.fn.modalform({'formURL': portal + 'modallogin.html',
                      'buttonName':'form.zojax-auth-login'});
      var uid = form.attr('id');
      var interval = window.setInterval(function() {
          loc = window.frames[uid+"-VIEW"].location.href;
          if (!loc.match(/modallogin/) && !loc.match(/about:blank/)) {
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
