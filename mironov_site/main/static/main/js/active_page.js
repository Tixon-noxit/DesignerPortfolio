 $(document).ready(function () {
     $('.site-menu a').each(function () {
         let location = window.location.protocol + '//' + window.location.host + window.location.pathname;
         let link = this.href;
         if(location === link) {
             $(this).parent().addClass('active')
         }
     })
 })