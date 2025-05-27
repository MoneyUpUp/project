// src/utils/useKakaoScript.js

export function loadScript({ id, src, onLoad }) {
  return new Promise((resolve, reject) => {
    if (document.getElementById(id)) {
      resolve();
      return;
    }

    const script = document.createElement("script");
    script.id = id;
    script.src = src;
    script.async = true;
    script.onload = () => {
      onLoad && onLoad();
      resolve();
    };
    script.onerror = reject;
    document.head.appendChild(script);
  });
}

export function removeScript(id) {
  const script = document.getElementById(id);
  if (script) {
    script.remove();
  }
}
