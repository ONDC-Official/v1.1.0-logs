**/init**
- City code mismatch in /search and /init
- gps coordinates in fulfillments[0].end.location mismatch in /select & /init
- address.area_code in fulfillments[0].end.location mismatch in /select & /init

**/on_init**
- City code mismatch in search & on_init
- gps coordinates in fulfillments[0].end.location mismatch in /select & /on_init
- address.area_code in fulfillments[0].end.location mismatch in /select & /on_init

**/confirm**
- City code mismatch in /search and /confirm
- address/door mismatches in /billing in /init and /confirm
- fulfillments[0].end.location.address.area_code is not matching with area_code in /select

**/on_confirm**
- City code mismatch in /search and /on_confirm
- fulfillments[0].end.location gps is not matching with gps in /select
- fulfillments[0].end.location.address.area_code is not matching with area_code in /select

**/status**
- City code mismatch in /search and /status

**/on_status (Order-picked-up)**
- City code mismatch in search and /on_status_picked

**/on_status (Order-Delivered)**
- City code mismatch in search and /on_status_delivered
- order/updated_at timestamp can't be less than the delivery time

**/update**
- City code mismatch in /search and /update

