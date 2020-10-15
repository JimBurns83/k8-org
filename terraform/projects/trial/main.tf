provider "kubernetes" {
   load_config_file = "false"

  host = "http://192.168.178.53:2375"

  username = "username"
  password = "password"
  
}

resource "kubernetes_namespace" "example" {
  metadata {
    name = "my-first-namespace"
  }
}