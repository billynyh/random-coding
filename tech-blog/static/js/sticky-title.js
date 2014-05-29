//http://stackoverflow.com/questions/13279725/getting-a-sticky-header-to-push-up-like-in-instagrams-iphone-app-using-css-a
function stickyTitles(stickies) {

    this.load = function() {

        stickies.each(function(){

            var thisSticky = jQuery(this).wrap('<div class="followWrap" />');
            thisSticky.parent().height(thisSticky.outerHeight());
            var t = thisSticky.offset().top;
            jQuery.data(thisSticky[0], 'pos', t);

        });
    }

    this.scroll = function() {

        stickies.each(function(i){
            var thisSticky = jQuery(this),
                nextSticky = stickies.eq(i+1),
                prevSticky = stickies.eq(i-1),
                pos = jQuery.data(thisSticky[0], 'pos');

            if (pos <= jQuery(window).scrollTop()) {
                thisSticky.addClass("fixed");
                if (nextSticky.length > 0 && thisSticky.offset().top >= jQuery.data(nextSticky[0], 'pos') - thisSticky.outerHeight()) {
                    thisSticky.addClass("absolute").css("top", jQuery.data(nextSticky[0], 'pos') - thisSticky.outerHeight());
                }
            } else {
                thisSticky.removeClass("fixed");
                if (prevSticky.length > 0 && jQuery(window).scrollTop() <= jQuery.data(thisSticky[0], 'pos')  - prevSticky.outerHeight()) {
                    prevSticky.removeClass("absolute").removeAttr("style");

                }
            }
        });         
    }
}

$(window).load(function() {
      //sticky headers
    var newStickies = new stickyTitles($(".sticky"));

    newStickies.load();

    $(window).on("scroll", function() {
        newStickies.scroll();
    });

    $(window).resize(function() {
      newStickies.resize();
    });

});
