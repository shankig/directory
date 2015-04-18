var App = (function () {

    var BASE_URL = "/api/"

    var build_table = function (data) {
        $("table#search_table tbody").html("");
        
        if (!data) {
            $("table#search_table tbody").append("No Records found");
        }
        
        $.each(data, function(index, value) {
            var data_str = "<tr>" +
                "<td>" + value['office_name'] + "</td>" +
                "<td>" + value['pincode'] + "</td>" +
                "<td>" + value['office_type'] + "</td>" +
                "<td>" + value['delivery_status'] + "</td>" +
                "<td>" + value['division_name'] + "</td>" +
                "<td>" + value['region_name'] + "</td>" +
                "<td>" + value['circle_name'] + "</td>" +
                "<td>" + value['taluk'] + "</td>" +
                "<td>" + value['district_name'] + "</td>" +
                "<td>" + value['state_name'] + "</td>" +
                "</tr>";        
            $("table#search_table tbody").append(data_str);
        });
    };

    var search_record = function () {
        var district = $("#district").val();
        var state = $("#state").val();
        var pincode = $("#pincode").val();
        var locality = $("#locality").val();
        var request_data = {};
        
        if (!district && !state && !pincode && !locality) {
            return;
        } else {
            if (district) {
                request_data["district"] = district
            }
            
            if (state) {
                request_data["state"] = state
            }
            
            if (pincode) {
                request_data["pincode"] = pincode
            }
            
            if (locality) {
                request_data["locality"] = locality
            }
        }
        
        $.getJSON(BASE_URL, request_data, function(data) {
            build_table(data)
        });
    };

    return {
        "search_record": search_record
    };
})(App);



