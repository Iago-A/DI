package com.example.aerocatalogo.models;

public class Plane {
    private String title;
    private String description;
    private String url;

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
}
