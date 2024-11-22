  $(document).ready(function () {
    $("#hero-image").on("click", function () {
        $('html, body').animate({
            scrollTop: ($('header').height() + 200)
        }, 1000, function () {
            $('html, body').animate({
                scrollTop: ($('header').height() + 600)
            }, 3000);
        });
    });
    let lastScrollY = $(window).scrollTop();

    $(window).on("scroll", function () {
      let currentScrollY = $(window).scrollTop();

      if (currentScrollY > lastScrollY) {
        // Scrolling down
        $("#header").addClass("hidden");
      } else {
        // Scrolling up
        $("#header").removeClass("hidden");
      }

      lastScrollY = currentScrollY; // Update the last scroll position
    });
  });


