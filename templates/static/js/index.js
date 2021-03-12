
class Index {
    constructor() {
        this.layout = new Layout();
    }

    start() {
        this.getTemperature();
        this.layout.test();

        setInterval(this.getTemperature, 1000);
    } 

    getTemperature() {
        let temp = $("#temp_val").text();
        $.ajax({
            type: "GET",
            url: $HOST_API + '/get/temperature',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            // data: JSON.stringify(data),
            success: function(response) {
                if (response.response.data) {
                    $("#temp_val").text(response.response.data + " °C");
                }
            },
            error: function(err) {
                console.log(err);
            }
        });
    }
}

$(document).ready(function(){
    let index = new Index();
    index.start();
});
