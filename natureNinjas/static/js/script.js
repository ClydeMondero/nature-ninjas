  $(document).ready(function () {
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


