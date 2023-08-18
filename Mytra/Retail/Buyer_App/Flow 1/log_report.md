**/search**
- /message/intent must have required property 'item'
- /message/intent/fulfillment must have required property 'end'

**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec

**/on_update (Return_Approved)**
- /fulfillments/1/start/location must have required property 'descriptor'

**/on_update (Return_Picked)**
- /fulfillments/1/start/location must have required property 'descriptor'

**/on_update (Return_Delivered)**
- /fulfillments/1/start/location must have required property 'descriptor'

