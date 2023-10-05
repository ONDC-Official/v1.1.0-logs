**/init**
- gps coordinates in fulfillments[0].end.location mismatch in /select & /init
- address.area_code in fulfillments[0].end.location mismatch in /select & /init

**/on_init**
- gps coordinates in fulfillments[0].end.location mismatch in /select & /on_init
- address.area_code in fulfillments[0].end.location mismatch in /select & /on_init

**/confirm**
- address/door mismatches in /billing in /init and /confirm
- fulfillments[0].end.location.address.area_code is not matching with area_code in /select

**/on_confirm**
- fulfillments[0].end.location gps is not matching with gps in /select
- fulfillments[0].end.location.address.area_code is not matching with area_code in /select

