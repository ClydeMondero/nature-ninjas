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


   let playing = false; // Prevent overlapping sounds

  $(".list-item").on("mouseenter", function () {
    if (playing) return; // Prevent multiple sounds from playing at once

    playing = true;
    const menuItem = $(this).data("menu"); // Get the menu name (e.g., "home", "explore")

    // Get the hover sound and the corresponding voice sound
    const hoverSound = document.getElementById("hover-sound");
    const voiceSound = document.getElementById(`${menuItem}-sound`);

       // Set volumes
    hoverSound.volume = 0.2; // Set hover sound to 40% volume
    voiceSound.volume = 0.8; // Set voice sound to 70% volume

    // Play the hover sound first
    hoverSound.currentTime = 0; // Restart hover sound from the beginning
    hoverSound.play();

    // When hover sound ends, play the corresponding voice sound
    hoverSound.onended = function () {
      voiceSound.currentTime = 0; // Restart voice sound from the beginning
      voiceSound.play();

      // Reset "playing" state when voice sound ends
      voiceSound.onended = function () {
        playing = false;
      };
    };

    // Handle any errors with the audio files
    hoverSound.onerror = function () {
      console.error("Error playing hover sound.");
      playing = false;
    };

    voiceSound.onerror = function () {
      console.error(`Error playing voice sound for menu item: ${menuItem}`);
      playing = false;
    };
  }); 

    const $heroVideo = $('#hero-video-element');

    if ($heroVideo.length) {
      setTimeout(function () {
                $heroVideo.prop('muted', true); // Mute the video
      }, 15000); // Stop video after 15 seconds
    }
  });


