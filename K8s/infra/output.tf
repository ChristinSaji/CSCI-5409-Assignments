output "region" {
  value       = var.gcp_region
  description = "GCloud Region"
}

output "project_id" {
  value       = var.gcp_project
  description = "GCloud Project ID"
}

output "kubernetes_cluster_name" {
  value       = google_container_cluster.k8s.name
  description = "GKE Cluster Name"
}

output "kubernetes_cluster_endpoint" {
  value       = google_container_cluster.k8s.endpoint
  description = "GKE Cluster Host"
}

output "kubernetes_cluster_master_version" {
  value       = google_container_cluster.k8s.master_version
  description = "GKE Cluster Master Version"
}
