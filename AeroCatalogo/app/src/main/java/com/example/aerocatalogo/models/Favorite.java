package com.example.aerocatalogo.models;

public class Favorite {
    private String id;
    private boolean isFavorite;

    public Favorite(String id, boolean isFavorite) {
        this.id = id;
        this.isFavorite = isFavorite;
    }

    // Getters and setters
    public String getId() {
        return id;
    }

    public boolean isFavorite() {
        return isFavorite;
    }

    public void setFavorite(boolean favorite) {
        isFavorite = favorite;
    }
}
