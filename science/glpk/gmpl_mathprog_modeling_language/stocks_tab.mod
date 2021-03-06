# USAGE: glpsol -m stocks_tab.mod -o stocks_tab.sol

/* *** DATA DECLARATION ************************* */

set T;                /* time */
param initial_state;
param stock_max;
param battery_max_in;
param battery_max_out;
param market_price {T};

/* *** DECISION VARIABLES *********************** */

var decision{t in T} >= -battery_max_out, <= battery_max_in;
var state{t in T} >= 0, <= stock_max;

/* *** OBJECTIVE FUNCTION *********************** */

maximize profit_total: sum{t in T} (market_price[t] * -decision[t]);

/* *** CONSTRAINTS ****************************** */

s.t. constraint_transition_initial: state[0] - initial_state - decision[0] = 0;
s.t. constraint_transition{t in T diff {0}}: state[t] - state[t-1] - decision[t] = 0;

/* *** DATA SECTION ***************************** */

data;

param : T : market_price :=
        0   10
        1   20
        2   10
        3   20
        4   10
;

param initial_state := 0;
param stock_max := 30;
param battery_max_in := 10;
param battery_max_out := 10;

end;

