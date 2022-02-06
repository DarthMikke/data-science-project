# Kor mange stillingar skal hentast? Set til 0 for å hente alle.
TOTAL <- 200

#require("httr")
#require("jsonlite")
source("Arbeidsplassen.r")


timestamp <- format(Sys.time(), "%Y-%m-%dT%H:%M:%S")
fetched <- -1

columns <- c("reference", "county", "municipal", "postal_code", "businessName", "source", "title", "uuid")

hits <- data.frame(matrix(nrow=0, ncol=length(columns)))
names(hits) <- columns

while (fetched < TOTAL) {
    search_query = ""
    if (fetched > 0) {
        search_query <- paste("from", "=", fetched, sep='')
    } else if (fetched == -1) {
        fetched <- 0
    }
    cat(fetched, "/", TOTAL, "\n", sep="")

    response <- sok(search_query)

    if (TOTAL == 0) {
        TOTAL <- response[['hits']][['total']][['value']]
    }

    new_hits <- Map(function(x) { x$"_source" }, response[['hits']][['hits']])
    new_hits <- Map(function(x) {
        list(
          x[['reference']],
          x[['locationList']][[1]][['county']],
          x[['locationList']][[1]][['municipal']],
          x[['locationList']][[1]][['postalCode']],
          x[['businessName']],
          x[['source']],
          x[['title']],
          x[['uuid']]
        )
      }, new_hits)
    new_hits <- Map(function(x) {
      li <- Map(function(y) {
        if (is.null(y)) {
          0
        } else {
          y
        }
      }, x)
      unlist(li)
      }, new_hits)
    new_hits <- as.data.frame(new_hits)
    new_hits <- as.data.frame(t(new_hits))
    colnames(new_hits) <- columns

    hits <- rbind(hits, new_hits)
    rownames(hits) <- NULL
    fetched <- fetched + nrow(new_hits)
}
cat(fetched, "/", TOTAL, "\n", sep="")

print(head(hits))
NEW_FILENAME <- paste('resultat/search_results-', timestamp, '.csv', sep='')
write.csv(hits, NEW_FILENAME, row.names=TRUE)
printf("Lagra søkeresultat i %s.", NEW_FILENAME)
