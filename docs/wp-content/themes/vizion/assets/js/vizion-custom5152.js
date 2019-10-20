/*
Template: Vizion - AI Startups Responsive WordPress Theme
Author: iqonicthemes.in
Version: 1.0
Design and Developed by: iqonicthemes.in
*/

/*----------------------------------------------
Index Of Script
------------------------------------------------

1.Page Loader
2.Back To Top
3.Background Overlay
3.Tooltip
4.Accordion
5.Header
6.Magnific Popup
7.Countdown
8.counter
9.Owl Carousel
10.Wow Animation
11.Tab Features
12.Contact From


------------------------------------------------
Index Of Script
----------------------------------------------*/
(function($) {

    "use strict";
    jQuery(document).ready(function() {
            jQuery(window).on('load', function(e) {

                /*------------------------
                Page Loader
                --------------------------*/
                jQuery("#load").fadeOut();
                jQuery("#loading").delay(0).fadeOut("slow");

                jQuery(".navbar a").on("click", function(event) {
                    if (!jQuery(event.target).closest(".nav-item.dropdown").length) {
                        jQuery(".navbar-collapse").collapse('hide');
                    }
                });

                /*------------------------
                Back To Top
                --------------------------*/
                jQuery('#back-to-top').fadeOut();
                jQuery(window).on("scroll", function() {
                    if (jQuery(this).scrollTop() > 250) {
                        jQuery('#back-to-top').fadeIn(1400);
                    } else {
                        jQuery('#back-to-top').fadeOut(400);
                    }
                });

                // scroll body to 0px on click
                jQuery('#top').on('click', function() {
                    jQuery('top').tooltip('hide');
                    jQuery('body,html').animate({
                        scrollTop: 0
                    }, 800);
                    return false;
                });

             /*------------------------
        Slick Slider
        --------------------------*/
        jQuery(".slick-slider").slick({
        dots: false,
        arrows: false,
        infinite: true,
        autoplay:true,
        prevArrow: false,
        nextArrow: false,
        centerMode: true,
        slidesToShow: 3,
        slidesToScroll: 3,
         responsive: [
         {
              breakpoint: 1024,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 1
                }
            },



            {
              breakpoint: 980,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            }

          ]
      });


        /*------------------------
        5 slider slick computer vizion
        --------------------------*/
          $('.slider-for').slick({
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
          prevArrow: false,
        nextArrow: false,
          fade: true,
          asNavFor: '.slider-nav'
        });
        $('.slider-nav').slick({
          slidesToShow: 8,
          slidesToScroll: 1,
          asNavFor: '.slider-for',
          dots: false,
          centerMode: true,
          focusOnSelect: true,
          responsive: [{
            breakpoint: 1024,
            settings: {
                slidesToShow: 5,
                slidesToScroll: 5,
            }
        }, {
            breakpoint: 640,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 4,
            }
        }, {
            breakpoint: 420,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
        }
        }]


        });


                /*************************
                        Background Overlay
                    *************************/
                jQuery.each(jQuery('.iq-background-overlay'), function() {
                    var $i;
                    var $p;
                    $i = jQuery(this).attr('id');
                    $i = '#' + $i;
                    $p = jQuery($i).parent().parent().parent().addClass($i);
                    jQuery($i).parent().parent().parent().addClass('section_overlay');
                    jQuery($i).insertBefore($p);
                });

                jQuery.each(jQuery('.layer_wrap'), function() {
                    var $i;
                    var $p;
                    $i = jQuery(this).attr('id');
                    $i = '#' + $i;
                    $p = jQuery($i).parent().parent().parent().addClass($i);
                    jQuery($i).parent().parent().parent().addClass('section_overlay');
                    jQuery($i).insertBefore($p);
                });

                /*------------------------
                Tooltip
                --------------------------*/

                jQuery(function() {
                    jQuery('[data-toggle="tooltip"]').tooltip()
                });

                /*------------------------
                Accordion
                --------------------------*/
                jQuery('.iq-accordion .iq-ad-block .ad-details').hide();
                jQuery('.iq-accordion .iq-ad-block:first').addClass('ad-active').children().slideDown('slow');
                jQuery('.iq-accordion .iq-ad-block').on("click", function() {
                    if (jQuery(this).children('div').is(':hidden')) {
                        jQuery('.iq-accordion .iq-ad-block').removeClass('ad-active').children('div').slideUp('slow');
                        jQuery(this).toggleClass('ad-active').children('div').slideDown('slow');
                    }
                });


                /*------------------------
                Header
                --------------------------*/

                jQuery(window).on('scroll', function() {
                    if (jQuery(this).scrollTop() > 10) {
                        jQuery('header').addClass('menu-sticky');
                    } else {
                        jQuery('header').removeClass('menu-sticky');
                    }
                });

                /*------------------------
                Magnific Popup
                --------------------------*/

                jQuery('.popup-gallery').magnificPopup({
                    delegate: 'a.popup-img',
                    type: 'image',
                    tLoading: 'Loading image #%curr%...',
                    mainClass: 'mfp-img-mobile',
                    gallery: {
                        enabled: true,
                        navigateByImgClick: true,
                        preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
                    },
                    image: {
                        tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
                        titleSrc: function(item) {
                            return item.el.attr('title') + '<small>by Marsel Van Oosten</small>';
                        }
                    }
                });


                jQuery('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
                    disableOn: 700,
                    type: 'iframe',
                    mainClass: 'mfp-fade',
                    removalDelay: 160,
                    preloader: false,
                    fixedContentPos: false
                });


                /*------------------------
                Countdown
                --------------------------*/
                jQuery('#countdown').countdown({
                    date: '10/01/2019 23:59:59',
                    day: 'Day',
                    days: 'Days'
                });

                /*------------------------
                counter
                --------------------------*/
                jQuery('.timer').countTo();


                /*------------------------
        8 Auto tab
        --------------------------*/

            var HM = {
    //tab
    jqs_slideList: '.slideList',
    jqs_tabList: '.slides .carouselLinks',


    init: function() {
        //init sliders
        var aSliders = $(this.jqs_slideList);
        if (aSliders.length > 0) {
            this.slideShow(aSliders);
        }

        //init the carousels that are lists of links
        // $('.carousel.icons').hellmannsCrsl({
        //     rotateSpeed: 5000,
        //     viewport: '.carouselLinks'
        // });
    },

    slideShow: function(eSlideListParam) {
        var slideList = eSlideListParam,
            slides = slideList.find('li'),
            tabList = slideList.siblings('.carouselLinks'),
            tabs = tabList.find('.object-new'),
            speed = 500;


        tabs.on('click', 'a', function(e) {
            $(this).trigger('slides.swap');
            e.preventDefault();
        });

        //make it automatic, but this doesn't work properly, I'm stuck...
        setInterval(function() {
            var current = parseInt($('li.selected a').data('links-to').split('_')[1],10);
            var idx=current-1;
            var max = $('.carouselLinks li a').length;
            idx = (current<max) ? (idx+1):0;
            $('.object-new a:eq('+idx+')').trigger('click');
        }, 3000);

        /**
         * This is where the animation, i.e. fade, is performing.
         * I find it quite convenient to use bind/trigger principle as it's easier to maintain
         */
        tabs.find('a').bind('slides.swap', function() {
            var self = $(this),
                selfIndex = self.parent().index(),
                targetSlide = slides.eq(selfIndex);

            //fade in/out slides
            slides.filter('.active').stop(true, false).fadeOut(speed, function() {
                $(this).removeClass('active');
            });
            targetSlide.stop(true, false).fadeIn(speed).addClass('active');

            tabs.removeClass('selected');
            self.parent().addClass('selected');
        });
    }
};

HM.init();

                /*------------------------
                Owl Carousel
                --------------------------*/
                jQuery('.owl-carousel').each(function() {
                    var $carousel = jQuery(this);
                    $carousel.owlCarousel({
                        items: $carousel.data("items"),
                        loop: $carousel.data("loop"),
                        margin: $carousel.data("margin"),
                        nav: $carousel.data("nav"),
                        dots: $carousel.data("dots"),
                        autoplay: $carousel.data("autoplay"),
                        autoplayTimeout: $carousel.data("autoplay-timeout"),
                        navText: ["<i class='fa fa-angle-left fa-2x'></i>", "<i class='fa fa-angle-right fa-2x'></i>"],
                        responsiveClass: true,
                        responsive: {
                            // breakpoint from 0 up
                            0: {
                                items: $carousel.data("items-mobile-sm"),
                                nav: false,
                                dots: true
                            },
                            // breakpoint from 480 up
                            480: {
                                items: $carousel.data("items-mobile"),
                                nav: false,
                                dots: true
                            },
                            // breakpoint from 786 up
                            786: {
                                items: $carousel.data("items-tab")
                            },
                            // breakpoint from 1023 up
                            1023: {
                                items: $carousel.data("items-laptop")
                            },
                            1199: {
                                items: $carousel.data("items")
                            }
                        }
                    });
                });

                /*------------------------
                Wow Animation
                --------------------------*/
                var wow = new WOW({
                    boxClass: 'wow',
                    animateClass: 'animated',
                    offset: 0,
                    mobile: false,
                    live: true
                });
                wow.init();

                /*------------------------
                Tab Features
                --------------------------*/
                jQuery('#myTab li a').on('click', function() {
                    jQuery('#myTab li a').attr('aria-selected', false);
                    jQuery(this).attr('aria-selected', true);
                });

                jQuery(window).on('scroll', function(e) {

                    var nav = jQuery('#features');
                    if (nav.length) {
                        var contentNav = nav.offset().top - 250;
                        if (jQuery(this).scrollTop() >= (contentNav)) {
                            e.preventDefault();
                            jQuery('#features .row #myTab li a').removeClass('active');
                            jQuery('#features .row #myTab li').children('a[aria-selected=true]').addClass('active');
                        }
                    }
                });
                jQuery('.sub-menu').css('display', 'none');
                jQuery('.sub-menu').prev().addClass('isubmenu');
                jQuery(".sub-menu").before('<i class="fa fa-angle-down toggledrop" aria-hidden="true"></i>');


                jQuery('.widget .fa.fa-angle-down, #main .fa.fa-angle-down').on('click', function() {
                    jQuery(this).next('.children, .sub-menu').slideToggle();
                });

                jQuery("#top-menu .menu-item .toggledrop").off("click");
                if (jQuery(window).width() < 992) {
                    jQuery('#top-menu .menu-item .toggledrop').on('click', function(e) {
                        e.preventDefault();
                        jQuery(this).next('.children, .sub-menu').slideToggle();
                    });
                }

            });

            jQuery(window).on('resize', function() { "use strict";
            jQuery('.widget .fa.fa-angle-down, #main .fa.fa-angle-down').on('click', function() {
                jQuery(this).next('.children, .sub-menu').slideToggle();
            });

            jQuery("#top-menu .menu-item .toggledrop").off("click");
            if (jQuery(window).width() < 992) {
                jQuery('#top-menu .menu-item .toggledrop').on('click', function(e) {
                    e.preventDefault();
                    jQuery(this).next('.children, .sub-menu').slideToggle();
                });
            }
        });
    });

})(jQuery);