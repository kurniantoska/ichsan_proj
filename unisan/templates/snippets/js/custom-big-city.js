function adjustHeightOfPage(pageNo) {

    var offset = 80;
    var pageContentHeight = $(".cd-hero-slider li:nth-of-type(" + pageNo + ") .js-tm-page-content").height();

    if($(window).width() >= 992) { offset = 120; }
    else if($(window).width() < 480) { offset = 40; }

    // Get the page height
    var totalPageHeight = 335 + $('.cd-slider-nav').height()
                            + pageContentHeight + offset
                            + $('.tm-footer').height();

    // Adjust layout based on page height and window height
    if(totalPageHeight > $(window).height())
    {
        $('.cd-hero-slider').addClass('small-screen');
        $('.cd-hero-slider li:nth-of-type(' + pageNo + ')').css("min-height", totalPageHeight + "px");
    }
    else
    {
        $('.cd-hero-slider').removeClass('small-screen');
        $('.cd-hero-slider li:nth-of-type(' + pageNo + ')').css("min-height", "100%");
    }
}

function uploadVideo() {

    var videoWrapper = $('.cd-bg-video-wrapper');
    if( videoWrapper.is(':visible') ) {
        // if visible - we are not on a mobile device
        var videoUrl = videoWrapper.data('video'),

        video = $('<video autoplay loop><source src="'+videoUrl+'.mp4" type="video/mp4" /></video>');
        video.appendTo(videoWrapper);

        // play video if first slide
        if(videoWrapper.parent('.cd-bg-video.selected').length > 0) video.get(0).play();
    }
}

// Everything is loaded including images.
$(window).load(function(){

    adjustHeightOfPage(1); // Adjust page height

    // Background Video
    if($( window ).width() > 800) {
        uploadVideo();
    }

    /* Gallery One pop up
    -----------------------------------------*/
    $('.gallery-first').magnificPopup({
        delegate: 'a', // child items selector, by clicking on it popup will open
        type: 'image',
        gallery:{enabled:true}
    });

    /* Gallery Two pop up
    -----------------------------------------*/
    $('.gallery-second').magnificPopup({
        delegate: 'a', // child items selector, by clicking on it popup will open
        type: 'image',
        gallery:{enabled:true}
    });

    /* Collapse menu after click
    -----------------------------------------*/
    $('#tmNavbar a').click(function(){
        $('#tmNavbar').collapse('hide');

        adjustHeightOfPage($(this).data("no")); // Adjust page height
    });

    /* Browser resized
    -----------------------------------------*/
    $( window ).resize(function() {
        var currentPageNo = $(".cd-hero-slider li.selected .js-tm-page-content").data("page-no");

        // wait 3 seconds
        setTimeout(function() {
            adjustHeightOfPage( currentPageNo );
        }, 3000);

        if($( window ).width() > 800) {
           uploadVideo();
        }

    });

    // Play video only when visible
    // https://stackoverflow.com/questions/21163756/html5-and-javascript-to-play-videos-only-when-visible
    $('video').each(function(){
        if ($(this).is(":in-viewport")) {
            $(this)[0].play();
        } else {
            $(this)[0].pause();
        }
    })

    // Remove preloader (https://ihatetomatoes.net/create-custom-preloading-screen/)
    $('body').addClass('loaded');
    $('.tm-current-year').text(new Date().getFullYear());

});