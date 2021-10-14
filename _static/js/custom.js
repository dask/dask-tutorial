if (location.protocol == "http:") {
  if (
    !window.location.href.includes("localhost") &&
    !window.location.href.includes("127.0.0.1")
  ) {
    location.href =
      "https:" +
      window.location.href.substring(window.location.protocol.length);
  }
}
