when HTTP_REQUEST { 
  set file ""
  if {[regexp {filename=([^&]+)} [HTTP::uri] match value]} {
      set file $value
  }
  
  if { ($file starts_with "/") or ($file starts_with "../") } { 
    log local0. "[IP::client_addr] requested $file" 
    HTTP::respond 403 content "I'm sorry, but your request for $file contains invalid characters. Please try your request again.\n" 
    return
  } 

  if { [HTTP::method] equals "POST" } {
    HTTP::collect 256
  } 
} 

when HTTP_REQUEST_DATA { 
  set file ""
  if {[regexp {filename=([^&]+)} [HTTP::payload] match value]} {
      set file $value
  }
  
  if { ($file starts_with "/") or ($file starts_with "../") } { 
    log local0. "[IP::client_addr] requested $file" 
    HTTP::respond 403 content "I'm sorry, but your request for $file contains invalid characters. Please try your request again.\n" 
    return
  } 

  HTTP::release 
}
