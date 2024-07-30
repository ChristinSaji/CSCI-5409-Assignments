import React from "react";
import Navbar from "./Navbar";

function History() {
  return (
    <div>
      <Navbar />
      <div className="flex items-center justify-center min-h-screen bg-gray-950">
        <div className="w-full max-w-md p-8 space-y-3 rounded-xl bg-white shadow-lg">
          <h1 className="text-3xl font-bold text-center text-indigo-800">
            History
          </h1>
        </div>
      </div>
    </div>
  );
}

export default History;
