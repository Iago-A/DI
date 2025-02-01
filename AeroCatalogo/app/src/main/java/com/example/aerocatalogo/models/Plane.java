package com.example.aerocatalogo.models;

public class Plane {
    private String title;
    private String description;
    private String url;
    private String id;

    public Plane() {} // Constructor vacío necesario para Firebase

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public String getUrl() {
        return url;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
}
