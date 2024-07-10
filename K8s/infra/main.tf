resource "google_container_cluster" "k8s" {
  name     = "k8s-cluster"
  location = var.gcp_zone

  initial_node_count = 1
  remove_default_node_pool = true
  deletion_protection = false
  node_config {
    image_type   = var.gke_image_type
    machine_type = var.gke_machine_type
    disk_type = var.gke_disk_type
    disk_size_gb = var.gke_disk_size
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform",
    ]
  }
}

resource "google_container_node_pool" "k8s_nodes" {
  cluster  = google_container_cluster.k8s.name
  location = google_container_cluster.k8s.location

  node_count = var.gke_num_nodes
  node_config {
    image_type   = var.gke_image_type
    machine_type = var.gke_machine_type
    disk_type = var.gke_disk_type
    disk_size_gb = var.gke_disk_size
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform",
    ]
  }
}
