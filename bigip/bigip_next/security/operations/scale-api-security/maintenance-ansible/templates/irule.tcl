when HTTP_REQUEST {
  if { [HTTP::host] eq "app.domain.local" } {
    pool app-maintenance-pool
  } 
}
