**/on_search**
- /message/catalog/bpp~1providers/0/items/2/descriptor/images must NOT have more than 3 items

**/on_confirm**
- order.updated_at timestamp should be updated as per the context.timestamp (since default fulfillment state is added)

**/on_status (Order-picked-up)**
- /fulfillments/0/end must have required property 'time'

**/on_update (Initiated)**
- /quote must have required property 'ttl'

**/on_update (Liquidated)**
- /quote must have required property 'ttl'

