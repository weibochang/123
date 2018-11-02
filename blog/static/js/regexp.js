$(function () {
    $('.excerpt-1 img').not('.thumb').remove();
    // attr({ src: "test.jpg", alt: "Test Image" });

    // alert(qwe)
    // $('.excerpt-1 img').not('.thumb').attr({ src: "/static/images/bad_img/bad_img.png", alt: "进入详情页查看图片" ,style:"height:23px; width:23px"});
    $('.excerpt-1 p').each(function () {
        var maxwidth = 50;
        if ($(this).text().length > maxwidth) {
            $(this).text($(this).text().substring(0, maxwidth));
            $(this).html($(this).html() + "...");
        }
    });

    $('.excerpt-minic-index img').remove();
    $('.excerpt-minic-index p').each(function () {
        var maxwidth = 100;
        if ($(this).text().length > maxwidth) {
            $(this).text($(this).text().substring(0, maxwidth));
            $(this).html($(this).html() + "...");
        }
    });

});


