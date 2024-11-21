package com.example.mycatalog;

import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import com.bumptech.glide.Glide;
import com.bumptech.glide.request.RequestOptions;

public class CatalogFragment extends Fragment {

    public CatalogFragment() {
        // Required empty public constructor
    }

    public static CatalogFragment newInstance(String param1, String param2) {
        CatalogFragment fragment = new CatalogFragment();

        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {

        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Infla el layout para este fragmento
        View rootView = inflater.inflate(R.layout.fragment_catalog, container, false);

        // Encuentra la vista desde rootView
        ImageView imageView = rootView.findViewById(R.id.catImageView);

        // Usa Glide para cargar la imagen en el ImageView
        Glide.with(this)
                .load(R.drawable.black_cat)
                .apply(RequestOptions.circleCropTransform())
                .into(imageView);

        return rootView;
    }

}