$(document).ready(function () {
  // Boutton Menu
  $("#menuToggle").click(function () {
    $("#mainNav").stop(true, true).slideToggle();
  });

  // Boutton Haut de page
  $(window).scroll(function () {
    if ($(this).scrollTop() > 400) {
      // Si on a défilement vers le bas de 300px
      $("#btnTop").fadeIn(); // On affiche le bouton
    } else {
      $("#btnTop").fadeOut(); // On cache le bouton
    }
  });

  // Lorsque l'on clique sur le bouton, on retourne en haut de la page
  $("#btnTop").click(function () {
    $("body,html").animate(
      {
        scrollTop: 0,
      },
      600
    );
  });

  // Barre de progression
  $(window).scroll(function () {
    var winScroll = $(this).scrollTop();
    var height = $(document).height() - $(window).height();
    var scrolled = (winScroll / height) * 100;
    $("#progressBar").width(scrolled + "%");
  });

  // Overlay
  var video = $("#overlay video")[0];
  $("#showVideo").click(function (e) {
    e.preventDefault();
    $("#overlay").addClass("visible");
  });

  $("#overlay video").click(function (e) {
    e.stopPropagation();
    video.play();
  });

  $("#overlay").click(function () {
    $("#overlay").removeClass("visible");
    video.pause();
  });
});
