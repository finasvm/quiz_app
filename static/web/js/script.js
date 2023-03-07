$(document).ready(function () {

    $("input[name=questionoption]:radio").click(function () {
        if ($('input[name=questionoption]:checked')) {
            answer_options = $('input[name=questionoption]')
            for (i = 0; i < answer_options.length; i++) {
                if (answer_options[i].checked) {
                    selected_option = answer_options[i].value
                }
            }

            $.ajax({
                url: "/answer-check/" + selected_option,
                type: "GET",
                success: function (result) {
                    console.log(result)
                    if (result.status = 'success') {
                        if (result.message) {
                            $("#label" + result.option).addClass("correct-answer");
                            $('input[name=questionoption]').attr("disabled", true);
                        } else {
                            $("#label" + result.option).addClass("wrong-answer");
                            $('input[name=questionoption]').attr("disabled", true);
                        }

                    }
                }
            })

        }
    });
})
