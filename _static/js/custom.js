if (location.protocol == "http:") {
  if (!window.location.href.includes("localhost")) {
    location.href =
      "https:" +
      window.location.href.substring(window.location.protocol.length);
  }
}
