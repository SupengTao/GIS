function search() {

    $.getJSON('/KGQA_answer', {
        name: $("#search").val(),

    }, function (json) {

        $("#text1").html(json.data);

    });

}

$(document).keypress(function (e) {
    // 回车键事件
    if (e.which == 13) {
        search();
    }
});