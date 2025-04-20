import React from "react";

export default function UploadPage({ onResult, onFileSelected }) {
  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    onFileSelected(file); // <- передаём файл в App

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:8000/analyze/", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    onResult(data);
  };

  return (
    <div>
      <h2 className="text-xl font-semibold mb-2">Загрузите файл топологии</h2>
      <input type="file" accept=".json" onChange={handleFileChange} />
    </div>
  );
}
