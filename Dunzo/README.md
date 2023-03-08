## Test Case Scenarios
### Flow 1:
1. Logistics buyer initiates /search for standard delivery & LSP responds with all available options;
2. Logistics buyer selects an option (for P2P) and sends /init request, for which LSP responds with a quote;
3. Logistics buyer sends /confirm for placing order and LSP accepts order;
4. Logistics buyer triggers ready-to-ship;
5. LSP delivers order, updates order & fulfillment state thru to completion thru unsolicited /on_status;

### Flow 2:
1. Logistics buyer initiates /search for express delivery & LSP responds with all available options;
2. Logistics buyer selects an option (for P2H2P) and sends /init request, for which LSP responds with a quote;
3. Logistics buyer sends /confirm for placing order and LSP accepts order;
4. LSP cancels order thru unsolicited /on_cancel;
