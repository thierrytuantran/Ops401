-- File name: ssl-info.nse

-- Description: Nmap script to gather SSL certificate information

local function sslInfo(host, port)
  local ssl_info = ssl.get_cert(host, port)
  return ssl_info
end

portrule = function(host, port)
  return port.protocol == "tcp" and port.number == 443
end

action = function(host, port)
  local cert_info = sslInfo(host, port.number)
  if cert_info then
    return "SSL certificate information:\n" .. cert_info
  else
    return "No SSL certificate information available"
  end
end
