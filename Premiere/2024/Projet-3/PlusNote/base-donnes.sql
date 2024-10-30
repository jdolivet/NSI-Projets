-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 17/10/2024 às 04:38
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `plusnote`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `materias`
--

CREATE TABLE `materias` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `materias`
--

INSERT INTO `materias` (`id`, `nome`) VALUES
(5, 'Francês'),
(6, 'Inglês'),
(7, 'NSI');

-- --------------------------------------------------------

--
-- Estrutura para tabela `notas`
--

CREATE TABLE `notas` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `materia_id` int(11) NOT NULL,
  `nota` decimal(5,2) NOT NULL,
  `data_lancamento` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `notas`
--

INSERT INTO `notas` (`id`, `usuario_id`, `materia_id`, `nota`, `data_lancamento`) VALUES
(14, 19, 7, 20.00, '2024-10-17 01:33:49'),
(15, 19, 5, 15.00, '2024-10-17 01:35:12'),
(16, 19, 7, 10.00, '2024-10-17 01:35:38');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `sobrenome` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `tipo` enum('aluno','professor') NOT NULL,
  `senha` varchar(255) DEFAULT NULL,
  `data_criacao` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `nome`, `sobrenome`, `email`, `tipo`, `senha`, `data_criacao`) VALUES
(1, 'Admin', 'Root', 'admin@example.com', 'professor', '$2y$10$o5FwCeu03zp6YG1ffdIHY.q70TP.ntZYWaCXlJIlVt2DVze/oUKfC', '2024-10-16 19:54:16'),
(19, 'Alphone', 'Dumortier', 'sybsmascaro@gmail.com', 'aluno', '$2y$10$cnURzIId7vN6x2sBAkjuwOCvO8JLoX5IcQjfA65WQ5VMCp7GM03vG', '2024-10-17 01:33:37');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `notas`
--
ALTER TABLE `notas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`),
  ADD KEY `materia_id` (`materia_id`);

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `materias`
--
ALTER TABLE `materias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `notas`
--
ALTER TABLE `notas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `notas`
--
ALTER TABLE `notas`
  ADD CONSTRAINT `notas_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `notas_ibfk_2` FOREIGN KEY (`materia_id`) REFERENCES `materias` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
