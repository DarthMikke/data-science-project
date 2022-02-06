require(httr)
require(jsonlite)

printf <- function(...) {
  cat(sprintf(...))
}

get_json <- function (url, query) {
  response <- GET(paste(url, query, sep="?"))
  content(response)
}

sok <- function(search_query) {
  url <- "https://arbeidsplassen.nav.no/stillinger/api/search"
  query <- paste(
    "occupationFirstLevels[]=Helse%20og%20sosial",
    "occupationSecondLevels[]=Helse%20og%20sosial.Helse",
    "size=50", sep="&"
  )
  if (search_query != "") {
    query <- paste(query, search_query, sep="&")
  }
  response <- get_json(url, query)
  response
}
