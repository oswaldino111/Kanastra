import React, { useReducer } from 'react';

const initState = {
    lineNumber: 0,
    uploadedCount: 0,
    statusEnvio: 'Nenhum aquivo...',
    files: []
};

const FileContext = React.createContext();

function reducer(state, action) {

    switch (action.type) {
        case 'next':
            let nextIndex = state.lineNumber + 1;
            return { ...state, lineNumber: nextIndex};
        case 'new':
            let uploadedCount = state.uploadedCount + 1;
            let nova_lista = [...state.files, action.dados];
            let status_new = 'Aguardando inicio';
            return { ...state, uploadedCount: uploadedCount, files: nova_lista, statusEnvio: status_new };
        case 'start':
            let status = 'Enviando...';
            return { ...state, statusEnvio: status };
        case 'done':
            let status_done = 'Envio Finalizado';
            return { ...state, statusEnvio: status_done };
        default:
            throw new Error(`Unknown '${action.type}' action type`);
    };
};

export const FileProvider = ({children}) => {

    const [state, dispatch] = useReducer(reducer, initState);
    const { lineNumber, uploadedCount, statusEnvio, files } = state;    
    
    return (
      <FileContext.Provider value={{state, dispatch, lineNumber, uploadedCount, statusEnvio, files}}>
        {children}
      </FileContext.Provider>
    );
};

export const useFileContext = () => {
    const fileContext = React.useContext(FileContext);
    if (fileContext === undefined) {
      throw new Error('useOnboardingContext must be inside a FileProvider');
    }
    return fileContext;
};