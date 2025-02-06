package com.example.aerocatalogo.views;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.fragment.app.Fragment;

import com.example.aerocatalogo.R;

public class ProfileFragment extends Fragment {
    // Constructor vacío
    public ProfileFragment() {}

    // Se infla el layout del fragment
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        // Infla el layout del fragment
        View view = inflater.inflate(R.layout.fragment_profile, container, false);


        // Aquí configuras RecyclerView, adapters, etc.



        return view;
    }
}
