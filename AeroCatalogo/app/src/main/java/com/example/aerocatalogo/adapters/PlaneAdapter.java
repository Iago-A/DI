package com.example.aerocatalogo.adapters;

import android.view.LayoutInflater;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.databinding.DataBindingUtil;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.example.aerocatalogo.R;
import com.example.aerocatalogo.databinding.ItemPlaneBinding;
import com.example.aerocatalogo.models.Plane;

import java.util.List;

public class PlaneAdapter extends RecyclerView.Adapter<PlaneAdapter.PlaneViewHolder> {

    private List<Plane> planes;
    private OnItemClickListener listener;

    public PlaneAdapter(List<Plane> planes, OnItemClickListener listener) {
        this.planes = planes;
        this.listener = listener;
    }

    @NonNull
    @Override
    public PlaneViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        ItemPlaneBinding binding = DataBindingUtil.inflate(
                LayoutInflater.from(parent.getContext()),
                R.layout.item_plane,
                parent,
                false
        );
        return new PlaneViewHolder(binding);
    }

    @Override
    public void onBindViewHolder(@NonNull PlaneViewHolder holder, int position) {
        Plane plane = planes.get(position);
        holder.bind(plane);
    }

    @Override
    public int getItemCount() {
        return planes != null ? planes.size() : 0;
    }

    public interface OnItemClickListener {
        void onItemClick(Plane plane);
    }

    class PlaneViewHolder extends RecyclerView.ViewHolder {
        private final ItemPlaneBinding binding;

        public PlaneViewHolder(@NonNull ItemPlaneBinding binding) {
            super(binding.getRoot());
            this.binding = binding;

            // Configurar el evento de clic
            binding.getRoot().setOnClickListener(v -> {
                Plane plane = binding.getPlane();
                if (plane != null) {
                    listener.onItemClick(plane); // Pasamos el plane al listener
                }
            });
        }

        public void bind(Plane plane) {
            binding.setPlane(plane);
            Glide.with(binding.getRoot().getContext())
                    .load(plane.getUrl())
                    .centerCrop()
                    .into(binding.planeImage);
            binding.executePendingBindings();
        }
    }
}

