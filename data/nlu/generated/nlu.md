## intent:dim.kpi.adject
- what is [worst](selection:bottom) [year](dim:Year)
- who is my [worst](selection:bottom) [client](dim:CustomerName)

## intent:dim.kpi_table.adject
- Who is the [best](selection:top) [customer](dim:CustomerName) in [north](CustomerRegion:North) region
- what about [worst](selection:bottom) [customer](dim:CustomerName)
- Who are the [top](selection) [10](CARDINAL) [employees](dim:Name) in each [region](dim:CustomerRegion)

## intent:fact.kpi.single
- what is my [sales](fact:SalesAmount)
- Show me [sales](fact:SalesAmount)
- show me [average](agg:mean) of [sales](fact:SalesAmount)
- what is my last month [sales](fact:SalesAmount)

## intent:fact.table.group
- show me [sales](fact:SalesAmount) for each [region](dim:CustomerRegion) on [pie](graph) chart

## intent:greetings.hello
- Hello

## intent:greetings.how_are_you
- Hello how are you?

## synonym:CustomerName
- client

## synonym:CustomerRegion
- region

## synonym:SalesAmount
- sales

## synonym:Year
- year

## synonym:bottom
- worst

## synonym:mean
- average
